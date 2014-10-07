import shutil, os

source_folder = "./Brazil_NightClub_Fire/large"

dest_folder = "./large_subset"

count = 0

for file in os.listdir(source_folder):
    if count < 3000:
        file_path = os.path.join(source_folder, file)
        dest_path = os.path.join(dest_folder, file)
        shutil.copyfile(file_path, dest_path)
        count += 1
    else:
        break