import os
import mmap

dir_path = "./Brazil_NightClub_Fire/Brazil_NightClub_Fire/"
count = 0

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        file_path = os.path.join(dir_path, file)
        file_stats = os.stat(file_path)
        f = open(file_path)
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find("Fire") == -1 and s.find("fire") == -1:
            print "No 'fire' found in:", file, file_stats.st_size
            os.remove(file_path)
            count += 1

print "# Removed:", count