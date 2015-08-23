def dashes():
    print "-" * 10
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA':'San Francisco',
    'MI':'Detriot',
    'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

dashes()
print "NY State has: " , cities['NY']
print "OR State has: " , cities['OR']

dashes()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print state abbreviations
dashes()

for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print city in states
dashes()

for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both
dashes()

for state, abbrev in states.items():
    print "%s state is abbreviated %s and has %s city" % (state, abbrev, cities[abbrev])

dashes()
# try to get a state that doesn't exist in the dict
state = states.get('Texas', None)

if not state:
    print "Sorry, no 'Texas'"

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city
