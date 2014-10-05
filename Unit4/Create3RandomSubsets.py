#!/usr/bin/python

import shutil, os

source_folder = '../Texas_Wild_Fire_Slim'
dest_folder = '../random_small_subsets'

hPath = '../random_small_subsets/hayden_work'
jPath = '../random_small_subsets/jordan_work'
mPath = '../random_small_subsets/mike_work'

haydensWork = open('../random_small_subsets/hayden_laundry_list.txt', 'w')
jordansWork = open('../random_small_subsets/jordan_laundry_list.txt', 'w')
mikesWork = open('../random_small_subsets/mike_laundry_list.txt', 'w')

count = 0

for fileName in os.listdir(source_folder):
	if count >= 300:
		break

	if count % 3 == 0:
		haydensWork.write(fileName)
		haydensWork.write('\n')
		haydenFile = os.path.join(source_folder, fileName)
		haydenFileDest = os.path.join(hPath, fileName)
		shutil.copyfile(haydenFile, haydenFileDest)

	if count % 3 == 1:
		jordansWork.write(fileName)
		jordansWork.write('\n')
		jordanFile = os.path.join(source_folder, fileName)
		jordanFileDest = os.path.join(jPath, fileName)
		shutil.copyfile(jordanFile, jordanFileDest)

	if count % 3 == 2:
		mikesWork.write(fileName)
		mikesWork.write('\n')
		mikeFile = os.path.join(source_folder, fileName)
		mikeFileDest = os.path.join(mPath, fileName)
		shutil.copyfile(mikeFile, mikeFileDest)
	
	count += 1
