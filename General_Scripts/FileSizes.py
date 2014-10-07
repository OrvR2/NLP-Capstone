import os

dir_path = "./Brazil_NightClub_Fire/large/"
count = 0
output = './Brazil_NightClub_Fire/output.txt'
outputF = open(output, 'w')

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        file_path = os.path.join(dir_path, file)
        file_stats = os.stat(file_path)	
	outputF.write(str(file_stats.st_size))
	outputF.write(" ")
	outputF.write(file)
	outputF.write("\n")
        

print "# Removed:", count
