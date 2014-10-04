import os

dir_path = "./Texas_Wild_Fire"

output = open('./list_small.txt', 'w')

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
	output.write(file)
	output.write('\n')

output.close()
