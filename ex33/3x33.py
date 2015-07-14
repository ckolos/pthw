from sys import argv
i=0
script = argv[0]
iterator = int(argv[1])
stepper = int(argv[2])

numbers = []

def while_loop(iterator, stepper):
  global i
  while i < iterator:
    print "At the top i is %d" % iterator
    numbers.append(i)
    i+=stepper
    print "Numbers now: ", numbers
    print "At the bottom i in %d" % i

while_loop(iterator, stepper)
print "The numbers: "
for num in numbers:
  print num
