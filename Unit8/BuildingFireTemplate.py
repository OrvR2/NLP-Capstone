from nltk.tokenize import sent_tokenize, word_tokenize
import re, os, operator, nltk
from TextUtilsU3 import *
from pattern.en import conjugate

# The directory location for ClassEvent documents.
classEventDir = '../Unit7/Large_Articles'
# The set of stopwords.
stopwords = nltk.corpus.stopwords.words('english')

def main():

	'''
	A pattern that matches "in" OR "at" followed by a single word, two words, or one word + a comma one or two words.
	This is intended to match common location occurrences, like: "in Islip, New York", or "at Islip" 
	'''
	locationPatternString = "(in|at|around|near)(\sthe)?\s[A-Z][a-zA-Z]{3,}(\s\S{4,})?(,\s([A-Z][a-zA-Z]{3,}){1,2})?"

	'''
	A pattern that matches possible causes (or 'source') of the event. Phrases matched are: 
	"affected by ____", "result of ____", "caused by _____", "by ____"
	'''
	causePatternString = "\S+\s(electric(al)?|pyrotechnic(s)?|firework(s)?|arson|gas|negligence)"

	'''
	A pattern that matches possible fuel sources for the fire.
	'''
	fuelPatternString = "\S+\s(foam|insulation|carpet|natural\sgas)"

	'''
	A pattern that matches possible damage caused by the fire.
	OLD: damagePatternString = "damaged(\s[\S]{3,}){1,3}|\S+\sin\sdamages|(\S+\s){2,3}destroyed(\s[A-Za-z0-9]{3,}){1,4}|(\S+\s){1,3}burned(\s\S+){1,3}"
	'''
	damagePatternString = "(damaged|destroyed|burned|desecrated|scorched|engulfed)(\s\S+){1,2}"

	'''
	A pattern that matches possible loss of life.
	'''
	lossOfLifePatternString = "\s[1-9][0-9]{0,2}\skilled|\s[1-9][0-9]{0,2}(dead|(of\s)?deaths)"

	'''
	A pattern that matches closures as a result of the fire.
	'''
	closuresPatternString = "\S+\s(stairwell(s)?|elevator(s)?|window(s)?|exit(s)?|ladder(s)?)"

	'''
	A pattern that matches the area of impact of the fire
	'''
	areaOfImpactPatternString = "([0-9]+|(\S+(\sof)?))\s(floor(s)?|building(s)?|room(s)?|block(s)?)"

	'''
	A pattern that matches firefighting measures employed in battling the fire.
	'''
	#firefightingMeasuresPatternString = "([0-9]+|(\S+(\sof)?))\sfirefighters"
	firefightingMeasuresPatternString = "(\S+\s){1,3}((extinguish(ed|ing)?)rescue(d)?|douse(d)?)(\s\S+){1,6}"

	'''
	A pattenr that matches terms signifying the severity of the fire.
	'''
	severityPatternString = "(\S{4,}\s)fire"

	'''
	A pattern for 4-digit years
	'''
	yearPatternString = "\s\d{4}"
	
	'''
	A pattern for months
	'''
	monthPatternString = "(?:January|February|March|April|May|June|July|August|September|October|November|December)"
	
	# Compilation of regex patterns to improve repeated query efficiency.
	locationPattern = re.compile(locationPatternString)
	causePattern = re.compile(causePatternString)
	fuelPattern = re.compile(fuelPatternString)
	damagePattern = re.compile(damagePatternString)
	closuresPattern = re.compile(closuresPatternString)
	areaOfImpactPattern = re.compile(areaOfImpactPatternString)
	firefightingMeasuresPattern = re.compile(firefightingMeasuresPatternString)
	severityPattern = re.compile(severityPatternString)
	yearPattern = re.compile(yearPatternString)
	monthPattern = re.compile(monthPatternString)
	lossOfLifePattern = re.compile(lossOfLifePatternString)

	# A list of all files in the Class Event Directory
	listOfFiles = os.listdir(classEventDir)

	# A Dictionary to store a word and it's associated type as a tuple for the key, and the associated frequency
	# for the value.
	D = dict()

	# Loop through all of the files in the Class Event directory.
	for fileName in listOfFiles:

		# Ignores any non .txt files
		if not fileName.endswith('.txt'):
			continue

		# Stores the file's absolute path
		filePath = os.path.join(classEventDir, fileName)

		# Reads the file contents and tokenizes by sentence.
		fileContents = open(filePath.strip(), 'r').read()
		#Remove non-English words
		words = fileContents.split()
		fileContents = ""
		for w in words:
			if is_ascii(w):
				fileContents = fileContents + " " + w
		fileSentences = sent_tokenize(fileContents)
				
		# Calls the searchMatches function to 
		searchMatches(D, locationPattern, fileSentences, fileName, "location")
		searchMatches(D, causePattern, fileSentences, fileName, "cause")
		searchMatches(D, yearPattern, fileSentences, fileName, "year")
		searchMatches(D, monthPattern, fileSentences, fileName, "month")
		searchMatches(D, fuelPattern, fileSentences, fileName, "fuel")
		searchMatches(D, damagePattern, fileSentences, fileName, "damage")
		searchMatches(D, closuresPattern, fileSentences, fileName, "closures")
		searchMatches(D, areaOfImpactPattern, fileSentences, fileName, "area")
		searchMatches(D, firefightingMeasuresPattern, fileSentences, fileName, "firefighting")
		searchMatches(D, severityPattern, fileSentences, fileName, "severity")
		searchMatches(D, lossOfLifePattern, fileSentences, fileName, "deaths")

	print

	'''
	The following code is used to filter words by their Parts of Speech (POS) tag. This is useful because, for example,
	we can ignore any "location" data that is not a noun, as we know that a verb would not be useful in describing a location.
	However, the reason that is not used is because when tagging words individually with POS, we lose context.
	So if we were to tag the phrase "between 5 and 8", which describes the time of, we would tag each word individually, and lose
	the context.

	# Each element in the list is of the form: [Attribute Type, List of Words, POS Tag]
	listOfResults = []

	# Stores the result of listOfResults AFTER filtering unneeded parts of speech.
	refinedListOfResults = []

	waterwaysList = []
	causeList = []
	timeList = []
	locationList = []
	girthList = []

	# From the frequency dictionary, grab the attribute type and word, split the word (which could be several words
	# long, like "between 5 and 8") into words, and append a list containing [Attribute Type, List of Words, POS Tag]
	for typeAndWordTuple, freq in D.iteritems():
		typeOfInfo, word = typeAndWordTuple
		word = word_tokenize(word)
		listOfResults.append([typeOfInfo, word, nltk.pos_tag(word)])
		if (typeOfInfo == "time"):
			timeList.append(word[1:])

	# Sorts list of results by the Attribute Type
	listOfResults = sorted(listOfResults)


	# Creates a dictionary storing the Parts of Speech that are valuable for each specific attribute.
	typeOfInfoPOS = {}
	typeOfInfoPOS["location"] = {"NNP"}
	typeOfInfoPOS["girth"] = {"NN", "JJ"}
	typeOfInfoPOS["cause"] = {"NN", "JJ"}
	typeOfInfoPOS["waterways"] = {"NN"}


	for result in listOfResults:
		typeOfInfo = result[0]
		for resultTuple in result[2]:

			if typeOfInfoPOS.has_key(typeOfInfo) and resultTuple[1] in typeOfInfoPOS[typeOfInfo]:

				refinedListOfResults.append([typeOfInfo, resultTuple])

	print 

	for result in refinedListOfResults:
		typeOfInfo = result[0]
		if typeOfInfo == "location":
			locationList.append(result[1][0])
		elif typeOfInfo == "waterways":
			waterwaysList.append(result[1][0])
		elif typeOfInfo == "cause":
			causeList.append(result[1][0])
		elif typeOfInfo == "girth":
			girthList.append(result[1][0])

	for typeAndWordTuple, freq in D.iteritems():
		typeOfInfo, word = typeAndWordTuple
		if (typeOfInfo == "time"):
			timeList.append(word)
		elif (typeOfInfo == "location"):
			locationList.append(word)
		elif (typeOfInfo == "girth"):
			girthList.append(word)
		elif (typeOfInfo == "cause"):
			causeList.append(word)
		elif (typeOfInfo == "waterways"):
			waterwaysList.append(word)
	'''

	# Creates a frequency dictionary for each attribute type
	locationFreqDict = dict()
	causeFreqDict = dict()
	yearFreqDict = dict()
	monthFreqDict = dict()
	fuelFreqDict = dict()
	damageFreqDict = dict()
	closuresFreqDict = dict()
	areaFreqDict = dict()
	firefightingFreqDict = dict()
	severityFreqDict = dict()
	lossOfLifeFreqDict = dict()

	# Loops through the original frequency dictionary, and adds the correspond word and frequency
	# to the dictionary for the appropriate attribute type.
	for typeAndWordTuple, freq in D.iteritems():
		typeOfInfo, result = typeAndWordTuple

		if (typeOfInfo == "location" and result not in stopwords):
			try:
				locationFreqDict[result] += freq
			except:
				locationFreqDict[result] = freq

		if (typeOfInfo == "cause" and result not in stopwords):	
			try:
				causeFreqDict[result] += freq
			except:
				causeFreqDict[result] = freq

		if (typeOfInfo == "year" and result not in stopwords):	
			try:
				yearFreqDict[result] += freq
			except:
				yearFreqDict[result] = freq
		if (typeOfInfo == "month" and result not in stopwords):	
			try:
				monthFreqDict[result] += freq
			except:
				monthFreqDict[result] = freq

		if (typeOfInfo == "fuel" and result not in stopwords):
			try:
				fuelFreqDict[result] += freq
			except:
				fuelFreqDict[result] = freq

		if (typeOfInfo == "damage" and result not in stopwords):
			try:
				damageFreqDict[result] += freq
			except:
				damageFreqDict[result] = freq

		if (typeOfInfo == "closures" and result not in stopwords):
			try:
				closuresFreqDict[result] += freq
			except:
				closuresFreqDict[result] = freq

		if (typeOfInfo == "area" and result not in stopwords):
			try:
				areaFreqDict[result] += freq
			except:
				areaFreqDict[result] = freq

		if (typeOfInfo == "firefighting" and result not in stopwords):
			try:
				firefightingFreqDict[result] += freq
			except:
				firefightingFreqDict[result] = freq

		if (typeOfInfo == "severity" and result not in stopwords):
			try:
				severityFreqDict[result] += freq
			except:
				severityFreqDict[result] = freq

		if (typeOfInfo == "deaths" and result not in stopwords):
			try:
				lossOfLifeFreqDict[result] += freq
			except:
				lossOfLifeFreqDict[result] = freq

	print 

	# Sorts all of the frequency dictionaries by their frequency values in reverse order, so the greatest
	# frequency is first.
	locationFreqDict = sorted(locationFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	causeFreqDict = sorted(causeFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	yearFreqDict = sorted(yearFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	monthFreqDict = sorted(monthFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	fuelFreqDict = sorted(fuelFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	damageFreqDict = sorted(damageFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	closuresFreqDict = sorted(closuresFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	areaFreqDict = sorted(areaFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	firefightingFreqDict = sorted(firefightingFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	severityFreqDict = sorted(severityFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
	lossOfLifeFreqDict = sorted(lossOfLifeFreqDict.iteritems(), key=operator.itemgetter(1), reverse=True)

	# Prints the top 10 words for each attribute.
	print "Top 10 frequent values for each attribute:"
	print "Location:", locationFreqDict [:10], "\n"
	print "Cause:", causeFreqDict [:10], "\n"
	print "Year:", yearFreqDict [:10], "\n"
	print "Month:", monthFreqDict [:10], "\n"
	print "Fuel:", fuelFreqDict [:10], "\n"
	print "Damage:", damageFreqDict, "\n"
	print "Closures:", closuresFreqDict [:10], '\n'
	print "Area:", areaFreqDict [:10], "\n"
	print "Firefighting:", firefightingFreqDict [:10], "\n"
	print "Severity:", severityFreqDict [:10], "\n"
	print "Loss Of Life:", lossOfLifeFreqDict [:10], "\n"

	firefightingResult = firefightingFreqDict[0][0]

	firefightingResult = " ".join([conjugate(word, tense = "past") if tag == 'VBP' else word for word, tag in nltk.pos_tag(nltk.word_tokenize(firefightingResult))])

	# Prints the original template.
	print "Template before filling-out:"
	print "In <start time>, there was a fire started by <cause> in <geographic location>. This fire, caused by <fuel>, grew to encompass <area of impact>, <damage (land/homes)>, and <loss of life>. <firefighting measures>. The fire was extinguished in <end time>. <closures> as a result of the fire. Compared to previous fires in the area this fire was <severity>."
	# Prints the highest frequency result for each attribute in the formated template.
	print "Template after filling-out:"
	print "In {0} {1} there was a fire started by {2} {3}. This fire, fueled by {4}, grew to the size of {5} and {6} and there were {7}. {8}. {9} was made unavailable for a period of time. Compared to previous fires in the city it was a {10}.".format(monthFreqDict[0][0], yearFreqDict[0][0], causeFreqDict[0][0], locationFreqDict[0][0], fuelFreqDict[1][0], areaFreqDict[0][0], damageFreqDict[1][0], lossOfLifeFreqDict[0][0], firefightingResult, closuresFreqDict[0][0], severityFreqDict[0][0], causeFreqDict[1][0])
	

	
# Prints any matches in the files with their corresponding filename and location in the file.
# Also creates a frequency dictionary for words and their attributes.
def searchMatches(D, pattern, fileSentences, fileName, typeOfInfo):
	
	# Loop over all sentences in the file.
	for sentence in fileSentences:

		# Loop over all matches from the regex object.
		for match in pattern.finditer(sentence):

			# Splits the match into words
			result = match.group().split()
			
			# Filters any words of length 2 or less.
			# result = [w for w in result if len(w) > 2]
			
			# Joins filtered set words with spaces
			result = " ".join(w for w in result)

			# Display the filename and location in the file at which a match was found. 
			print "{4}: {0}: {1}-{2}: {3}".format(fileName, match.start(), match.end(), result, typeOfInfo)
			
			# Increment the frequency for this attribute and word pair
			try:
				D[typeOfInfo, result] += 1
			except:
				D[typeOfInfo, result] = 1

if __name__ == "__main__": main()