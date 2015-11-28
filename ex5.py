#!/usr/bin/env python

my_name = 'Evan'
my_age = 24 #not a lie 
my_height = 172 #cm
my_weight = 65 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
		my_age, my_height, my_weight, my_age + my_height + my_weight)

