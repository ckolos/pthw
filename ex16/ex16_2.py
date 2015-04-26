from sys import argv

script = argv

print "We're going to erase the file you input here: "
filename = raw_input("File?: ")

print "Are you sure you want to delete %s?" % filename 
print "If you do want that, hit RETURN"
print "If you don't want to delete %s, hit CTRL-C (^C)" % filename

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
