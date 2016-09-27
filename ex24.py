"""
   @Author: ShiLiNa
   @Brief:The exercise22 for Learn python the hard way
   @CreatedTime:27/09/2016
"""
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion form intuition
and requires an explanation
\n\t\t where there is none.
"""

print "_______________________"
print poem
print "_______________________"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula( started ):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print "With a starting point of:%d" % start_point
print "We'd have %d beans, %d jars,and %d crates. " %(jelly_beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d jelly_beans, %d jars, and %d crates." %secret_formula(start_point)