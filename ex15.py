"""
    @Author:ShiLiNa
    @Brief:The exercise15 for learn python the hard way
    @CreatedTime:28/7/2016
"""
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
