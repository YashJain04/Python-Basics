# Most work done on slides
# Covered through W3Schools

def myfunc(n):
  return lambda a : a * n

mynumber1 = myfunc(int(input("Enter a number: "))) 

print()
print(mynumber1(int(input("Enter a number: "))))