import math

# abs - return the absolute value of a number.
# The argument may be an integer or a floating
# point number.

print(abs(-23))
print(abs(3.44444))
print(abs(-3.44444))
#converts to float
print(abs(float('20')))

# fabs - converts to float.
# you need to import math
print(math.fabs(-4))

# sum - takes an iterable and an optional start.
# returns the sum of start and the items of an
# iterable from left to right and returns
# the total.
# start defaults to 0.

print(sum([1,2,3]))
#optional start, this will start at 10 and add 1,2,3.
print(sum([1,2,3],10))
#float
print(sum([1.5,3.7]))
#dict
print(sum({1,2,3}))

# round - return number rounded to ndigits precision
# after the decimal point. If ndigits is omitted or is
# None, it returns the nearest integer to its input.

print(round(10.2))
# round in 2 decimal places
print(round(1.212121,2))
# using None
print(round(3.52117,None))
# this will only round to 10.0
print(round(9.9999999999999999999999999999,15))

