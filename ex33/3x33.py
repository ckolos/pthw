from sys import argv
i=0
iterator=int(argv[1])
print argv
numbers = []

def while_loop(iterator):
  global i
  while i < iterator:
    print "At the top i is %d" % iterator
    numbers.append(i)
    i+=1
    print "Numbers now: ", numbers
    print "At the bottom i in %d" % i

while_loop(iterator)
print "The numbers: "
for num in numbers:
  print num
