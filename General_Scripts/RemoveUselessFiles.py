import os
import mmap

dir_path = "../Texas_Wild_Fire_Slim/"
count = 0

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        file_path = os.path.join(dir_path, file)
        file_stats = os.stat(file_path)
        f = open(file_path)
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find("Texas Forest Service") != -1:  
            os.remove(file_path)
            count += 1

print "# Removed:", count
