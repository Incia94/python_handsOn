import math

a = 10.5
b = 16
c = 20.0003
d = -5
e = -4.09
f = 29.9

# returns a sorted list of strings containing the names defined by math module
print(dir(math))
print('\n')
# Prints all math constants

print(math.pi)      # pi value
print(math.inf)     # denotes positive infinity
print(-math.inf)    # denotes negative infinity
print(math.nan)     # not a number
print(math.tau)     # tau's number
print(math.e)       # euler's number

print('\n')

# mathematical functions defined in math module
print(math.tan(45))
print(math.sin(60))
print(math.cos(30))
print(math.fabs(e))  # float absolute value
print(math.ceil(f))
print(math.floor(e))
print(math.factorial(3))
print(math.log2(4))
print(math.sqrt(49))
print(math.copysign(2, -4))     # return floating point number with value of 1st variable and sign of second variable
print(math.radians(180))
print(math.remainder(9, 4))
print(math.gcd(44, 24))
print(math.pow(8, 2))
print(math.isfinite(340000000000))
print(math.isfinite(math.inf))
print(math.exp(34))
print(math.trunc(0.9888))   # truncates to closest integer
list1 = [1, 2, 3]
print(math.fsum(list1))


