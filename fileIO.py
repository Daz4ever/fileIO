from sys import argv

script, filename = argv


openfile = open(filename)

filelines = openfile.readlines()

print len(filelines)
