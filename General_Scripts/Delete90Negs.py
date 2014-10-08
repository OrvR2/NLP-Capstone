import os, sys

target_dir = './random_small_subsets/combined_subset'

count = 0

for file in os.listdir(target_dir):
    if count >= 90:
        break
    
    file_path = os.path.join(target_dir, file)
    if (file.endswith("_neg.txt")):
        print 'Deleting', file
        os.remove(file_path)
	count += 1
