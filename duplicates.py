import os

def percentage(part, whole):
  return 100 * float(part)/float(whole)

dictionary = dict()
num_files = 0

for root, _, files in os.walk('Texas_Wild_Fire_Slim'):
	for f in files:
		num_files += 1
		fullpath = os.path.join(root, f)
		file_size = os.path.getsize(fullpath)
		try:
			dictionary[file_size] += 1
		except:
			dictionary[file_size] = 1

length = len(dictionary)
print 'Number of files: {0}'.format(num_files)
print 'Length of dictionary: {0}'.format(length)
print '% duplicates: {0}'.format(percentage(length, length + num_files))