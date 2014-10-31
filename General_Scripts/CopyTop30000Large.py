import shutil, os

source_folder = "../Brazil_NightClub_Fire/large"

dest_folder = "../Large_Slim"

list = '../Logs_Lists/top30000-large.txt'

with open(list, 'r') as file:
    for line in file:
	line = line.strip()
	size, file = line.split(" ")
	file_src = os.path.join(source_folder, file)
	file_dest = os.path.join(dest_folder, file)
	shutil.copyfile(file_src, file_dest)
