from sys import argv

script, user_name = argv
prompt = '-->'
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print "How big are your feet %s?" % user_name
feet = raw_input(prompt)

print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.

Plus you have size %s feet. I like feet.
''' % (likes, lives, computer, feet)

