#!/usr/bin/env python

# this one is like your script with argv
def print_two(*args):
    print args
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this oen takes on arguments
def print_none():
    print "I got nothing..."

print_two("evan", "lin")
print_two_again("evan", "lin")
print_one("evan")
print_none()
