#!/usr/bin/env python
import sys, zipimport, os, re

locationPatternString = "(in|at|around|near)(\s\S+){1,2}|[A-Z][a-zA-Z]{3,},\s[A-Z][a-zA-Z]{2,}(\s[A-Z][a-zA-Z]{3,})?|(\S+\s){1,3}forest|(\S+\s){1,2}(State|National)\sPark"
causePatternString = "(\S+\s){1,2}(electric(al)?|pyrotechnic(s)?|firework(s)?|arson|gas|negligen(t|ce))(\s\S+){1,2}"
fuelPatternString = "(\S+\s){1,2}(foam|insulation|carpet|natural\sgas)|(\S+\s){1,2}(caught\son\sfire)"
damagePatternString = "(\S+\s){1,2}dollar(s)?|\$[0-9]+(\s\S+){0,3}|damage(d|s)?(\s\S+){1,3}|(\S+\s){1,2}(destroy(ed|s)?|devastate(d|s)?)"
lossOfLifePatternString = "\s[0-9]{1,3}\s(\S+\s){0,2}killed|[0-9]+\s(\S+\s)(dead|(of\s)?deaths)"
closuresPatternString = "(\S+\s(stairwell(s)?|elevator(s)?|window(s)?|exit(s)?|ladder(s)?)(\s\S+){1,2})|(\S+\s){1,4}evacuate(d)?"
areaOfImpactPatternString = "(\S+\s){1,2}(floor(s)?|building(s)?|room(s)?|block(s)?)"
firefightingMeasuresPatternString = "(\S+\s){1,3}((extinguish(ed|ing)?)rescue(d)?|douse(d)?)(\s\S+){1,6}"
severityPatternString = "(\S+\s)?(severe|tragic|devastating)(\s\S+){1,2}."
yearPatternString = "\s\d{4}"
monthPatternString = "(?:January|February|March|April|May|June|July|August|September|October|November|December)"

locationPattern = re.compile(locationPatternString)
causePattern = re.compile(causePatternString)
fuelPattern = re.compile(fuelPatternString)
damagePattern = re.compile(damagePatternString)
lossOfLifePattern = re.compile(lossOfLifePatternString)
closuresPattern = re.compile(closuresPatternString)
areaOfImpactPattern = re.compile(areaOfImpactPatternString)
firefightingMeasuresPattern = re.compile(firefightingMeasuresPatternString)
severityPattern = re.compile(severityPatternString)
yearPattern = re.compile(yearPatternString)
monthPattern = re.compile(monthPatternString)

patterns = {"Location": locationPattern, "Cause": causePattern,
    "Fuel": fuelPattern, "Damage": damagePattern, "LossOfLife": lossOfLifePattern,
    "Closures": closuresPattern, "Area": areaOfImpactPattern,
    "Firefighting": firefightingMeasuresPattern, "Severity": severityPattern,
    "Year": yearPattern, "Month": monthPattern}

importer = zipimport.zipimporter('nltk.mod')
nltk = importer.load_module('nltk')
nltk.data.path += ["./nltkData/"]

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

f = sys.stdin
 
event_dir = './event'

for fileName in f.readlines():
    fileName = fileName.strip()
    counter, fileName = fileName.split()
    filePath = os.path.join(event_dir, fileName)
    file = open(filePath, 'r')
    fileWords = file.read().split()
    file.close()
    fileContents = ""
    for w in fileWords:
        if is_ascii(w):
            fileContents = fileContents + " " + w
    fileSentences = nltk.tokenize.sent_tokenize(fileContents)

    for sentence in fileSentences:
    
        for type, pattern in patterns.iteritems():
            for match in pattern.finditer(sentence):
                result = match.group().split()

                result = " ".join(w for w in result)
                result.strip()
                print "{0};{1};{2}".format(type, 1, result)
