__author__ = 'Quintin Martinus'

from sys import argv  # uses argv to get a file name

script, filename = argv  # uses argv to get a file name

txt = open(filename)  # uses argv to get a file name

print "Here's your file %r:" % filename
print txt.read()  # print whats written in the file

print "Type the filename again:"
file_again = raw_input("> ")  # you input a file name again under a new variable

txt_again = open(file_again)  # opens the file under the variable file_again and assigns it too the variable txt_again

print txt_again.read()  # prints  the file allocated to the variable txt_again
