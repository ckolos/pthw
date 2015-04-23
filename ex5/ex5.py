name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teet are usually %s, depending on the coffee" % teeth

print "If I add %d, %d, and %d, I get %d" % ( age, height, weight, age + height + weight)
total = age + height + weight
print "Testing out the %%r variable: %r" % "foo%1"

print "testing out the various python formatting characters"
print "Here is the number %d as a hex, lower case, using %%x: %x" % (total,total)
print "Here is the number %d as a hex, upper case, using %%X: %X" % (total,total)
