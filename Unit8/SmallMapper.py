#!/usr/bin/env python

#!/usr/bin/env python
import sys, zipimport, os, re

locationPatternString = "((in|at)\s([A-Z][a-zA-Z]{4,}|[A-Z][a-zA-Z]{2,}\s[A-Z][a-zA-Z]{3,}))|\s+[A-Z][a-zA-Z]{3,},\s[A-Z][a-zA-Z]{2,}\s[A-Z][a-zA-Z]{3,}|(around|near)(\sS+){1,2}|(\S+\s){1,3}forest|(\S+\s){1,2}(State|National)\sPark"
causePatternString = "(\S+\s){1,2}(wind(s)?|lightning|drought|arson(s)?|(negligence|negligent))(\s\S+){1,2}"
fuelPatternString = "(\S+\s){1,3}(wind|brush|trees|forest(s)?)"
damagePatternString = "damaged(\s[\S]{3,}){1,3}|\S+\sin\sdamages|(\S+\s){2,3}destroyed(\s[A-Za-z0-9]{3,}){1,4}|(\S+\s){1,4}burned(\s\S+){1,3}"
lossOfLifePatternString = "\s[0-9]{1,3}\s(\S+\s){0,2}killed|[0-9]+\s(\S+\s)(dead|(of\s)?deaths)"
closuresPatternString = "((\S+\s){1,2}(highway(s)?|freeway(s)?|interstate(s)?)(\s\S+){1,2})|(\S+\s){4,7}evacuate(d)?"
areaOfImpactPatternString = "(\S+\s){1,2}(miles|hectares)|(\S+\s){1,2}acres"
firefightingMeasuresPatternString = "(\.|\t|\n)(\S+\s)*firefighter(s)?(\s\S+)*(\.|\t|\n)|(\S+\s)extinguish(ed|ing)?(\s\S+){1,2}|(\.|\t|\n)(\S+\s)*(fire\sretardant|helicopter|plane)(\s\S+)*\."
severityPatternString = "(\S+\s)?(severe|tragic|devastating|raging|widespread)(\s\S+)."
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

f = sys.stdin.read()

words = f.split()
for w in words:
    if is_ascii(w):
        contents = contents + " " + w
    
fileSentences = nltk.tokenize.sent_tokenize(fileContents)

# Each line in sys.stdin will be the name of a document.
for sentence in fileSentences:
    
    for pattern in patterns.iteritems():
        for match in patterns[pattern].finditer(sentence):
            result = match.group().split()

            result = " ".join(w for w in result)
            result.strip()
            print "{0};{1};{2}".format(pattern, 1, result)
