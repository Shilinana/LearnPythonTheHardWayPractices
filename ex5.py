#-*- coding: utf-8 -*-
"""
   @Author:ShiLiNa
   @Brief:The exercise5 of Learn python the hard way
   @CreatedTime:16/7/2016
"""
my_name = 'Zed A.Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # 1bs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %r." % my_name
print "He's %r inches tall." % my_height
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age+my_height+my_weight)