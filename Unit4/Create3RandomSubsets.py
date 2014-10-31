#!/usr/bin/python

import shutil, os, random

source_folder = '../Large_Slim'
dest_folder = '../large_subsets/work'

work = open('../large_subsets/LaundryList.txt', 'w')

count = 0

file_list = os.listdir(source_folder)
random.shuffle(file_list)

for fileName in file_list:
    if count >= 300:
		break
 
    work.write(fileName)
    work.write('\n')
    file = os.path.join(source_folder, fileName)
    fileDest = os.path.join(dest_folder, fileName)
    shutil.copyfile(file, fileDest)
	
    count += 1
