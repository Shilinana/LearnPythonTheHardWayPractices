"""
   @Author:ShiLiNa
   @Brief:The exercise33 for Learn python the hard way
   @CreatedTimes:08/10/2016
"""
i = 0
numbers = []

while i < 6:

    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
print "Number now:", numbers
print "At the bottom i is %d" % i 

print "The numbers:"

for num in numbers:
    print num
