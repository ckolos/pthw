# number of cars available
cars = 100

# how many people can we cram in one car
space_in_a_car = 4.0

# how many drivers do we have
drivers = 30

# How many people are riding not driving
passengers = 90

# how many cars don't have drivers
cars_not_driven = cars - drivers

# each driver can only drive 1 car
cars_driven = drivers

# how many people can carpool?
carpool_capacity = cars_driven * space_in_a_car

# how many people will be riding in each of the available cars?
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

