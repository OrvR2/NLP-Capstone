import os

dir_path = "../Texas_Wild_Fire_Slim"

output = open('./list_small_slim.txt', 'w')

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
	output.write(file)
	output.write('\n')

output.close()
