import os

dir_path = "../Texas_Wild_Fire_Slim"
count = 0

dict_FileSize_NumFiles = {}

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        file_path = os.path.join(dir_path, file)
        file_stats = os.stat(file_path)

        size = file_stats.st_size

        if size in dict_FileSize_NumFiles:
        	filePath = os.path.join(dir_path, file)
        	os.remove(filePath)
        else:
        	dict_FileSize_NumFiles[size] = 1

#print dict_FileSize_NumFiles
