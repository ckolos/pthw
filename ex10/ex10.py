tabby_cat = "\tI'm  tabbed in"
persian_cat = "I'm split on\n a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

loud_cat = "\a"
hex_cat = "\x26"

print "boing", loud_cat
print "hex cat:", hex_cat

# create a complex format
format_list = "I am a list:\n\t* %r\n\t* %r\n\t* %r\n\t* %r"

print format_list % ("This", "is", "a", "list" )
print format_list % ("%r",'%r',"%r",'%r')
