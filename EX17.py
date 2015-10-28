__author__ = 'MrBIGL'

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?

# in_file = open(from_file)  # open from file
# indata = in_file.read()  # reads the data in the from file

# the information up there shortened

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)  # calculates how many bytes are in the from file

# print "Does the output file exist? %r" % exists(to_file)  # checks if the to file exists
# print "Ready, hit RETURN to continue, CTRL-C to abort."
print "Continue with copying?"
raw_input()

out_file = open(to_file, 'w')  # opens the outfile in writing mode (to be able to copy to it)_
out_file.write(indata)  # copys the data in from file to outfile which is to file openeed in writable mode

print "Alright, all done."

out_file.close()  # closes out file
# in_file.close()  # closes in file  / Commented out because it became irrelevant once it was included in the indata

