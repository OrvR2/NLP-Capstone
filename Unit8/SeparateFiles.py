import os

locationFile = open("SmallResults/location.txt", 'w')
causeFile = open('SmallResults/cause.txt', 'w')
fuelFile = open('SmallResults/fuel.txt', 'w')
damageFile = open('SmallResults/damage.txt', 'w')
lossOfLifeFile = open('SmallResults/lossoflife.txt', 'w')
closuresFile = open('SmallResults/closures.txt', 'w')
areaFile = open('SmallResults/area.txt', 'w')
firefightingFile = open('SmallResults/firefighting.txt', 'w')
severityFile = open('SmallResults/severity.txt', 'w')
yearFile = open('SmallResults/year.txt', 'w')
monthFile = open('SmallResults/month.txt', 'w')

fileDict = {'Location' : locationFile, 'Cause': causeFile, 'Fuel': fuelFile, 'Damage': damageFile, 'LossOfLife': lossOfLifeFile, 'Closures': closuresFile, 'Area': areaFile, 'Firefighting': firefightingFile, 'Severity': severityFile, 'Year': yearFile, 'Month': monthFile}

with open('./small_output/sorted.txt', 'r') as file:
    for line in file.readlines():
        type, count, result = line.strip().split('\t', 2)
        fileDict[type].write(line)

locationFile.close()
causeFile.close()
fuelFile.close()
damageFile.close()
lossOfLifeFile.close()
closuresFile.close()
areaFile.close()
firefightingFile.close()
severityFile.close()
yearFile.close()
monthFile.close()
