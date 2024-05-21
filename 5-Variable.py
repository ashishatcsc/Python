# 1. Create a variable (any name) and store a string in the variable.
# 2. Then, print out the type of the variable.

intx = 10
floatx = 10.0
welcomestring = "Hello World!!!"

print("This is an integer value", intx, "and its type is", type(intx))
print("This is a float value", floatx, "and its type is", type(floatx))
print("This is a string value", welcomestring, "and its type is", type(welcomestring))


print("Here are the value functions support by string class", dir(str), "\n\\n\\n")
print("Here are the value functions support by integer class", dir(int), "\n\\n\\n")
print("Here are the value functions support by float class", dir(float), "\n\\n\\n")

