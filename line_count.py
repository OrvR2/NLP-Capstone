import os

count = 0
total = 0

for root, _, files in os.walk('Unit7/Small_Articles'):
	for f in files:
		fullpath = os.path.join(root, f)
		num_lines = sum(1 for line in open(fullpath))
		count += 1
		total += num_lines

print "Average number of lines in directory {0}".format(total / count)