import os

for file in os.listdir("."):
    if file.endswith(".txt"):
        file_stats = os.stat(file)
        if file_stats.st_size == 0:
            print "Removing: ", file, file_stats.st_size
            os.remove(file)