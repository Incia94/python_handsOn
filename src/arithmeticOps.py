# Basic mathematical operations in Python

# Get user Input
a = input("fist number:")
b = input("second number:")

# sum of 2 numbers
sum = int(a) + int(b)
# subtract two numbers
diff = int(a) - int(b)
# Multiply two numbers
mul = float(a)*float(b)
# Divide two numbers
div1 = float(a)/float(b)
# Divide two numbers such that it returns the floor value
div2 = float(a)//float(b)
# modulus of two numbers
mod = int(a) % int(b)

# Results
print("The sum of {0} and {1} is {2}" .format(a, b, sum))
print("the subtraction of {0} and {1} is {2}".format(a, b, diff))
print("the multiplication of {0} and {1} is {2}".format(a, b, mul))
print("the division of {0} and {1} is {2}".format(a, b, div1))
print("the floor division of {0} and {1} is {2}".format(a, b, div2))
print("the modulo division of {0} and {1} is {2}".format(a, b, mod))

