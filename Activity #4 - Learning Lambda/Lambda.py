# Section 1 - Revisiting Problem #1

# set of countries (1 will repeat)
countries = {"Canada"}

# adding country
for i in range(0, 5):
    add_country = str(input("Enter a country: "))
    countries.add(add_country)

# print commands
print()
print(countries)
print()

# iterate over the set
for i in countries:
    print(i)

# Section 2 - Learning lambda

# add 10 to the argument "a", and return the result
x = lambda a : a + 10
print(x(5))
print()

# lambda functions can take any number of arguments
x = lambda a, b : a + b
print(x(5, 6))
print()

x = lambda a, b, c : a * b * c
print(x(1, 2, 3))
print()

# Section 3 - Using Lambda
# create a function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) # double it
mytripler = myfunc(3) # triple it

print()
print(mydoubler(11))
print(mytripler(11))