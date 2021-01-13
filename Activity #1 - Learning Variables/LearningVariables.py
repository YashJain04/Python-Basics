#String Variables (Single or Double Quotes Can Be Used)
a = "John"
b = 'Jackie'

#Number Variables
c = 5 #int type variable
d = 5.0 #float type variable
e = 1j #complex type variable

#Boolean Variables (True or Flase Values)
f = True
g = False

#Sequence Variables
h = ["apple", "banana", "cherry"] #list type variable
i = ("apple", "banana", "cherry") #tuple type variable
j = range(7) #range type variable

#Overwriting Variables
k = 5 #k is of type int
k = "Sally" #k is now of type str (String)
print(k) #prints Sally

l = 5 
L = "Sally"
print(l) #prints 5 because this is not overwriting - variables are case sensitive

#Casting Variables
m = str(3) #m will be '3'
n = int(3) #n will be 3
o = float(3) #o will be 3.0S

#Getting The Type of Variables
p = 5
q = "Jack"
print(type(p)) #prints that it is an integer type
print(type(q)) #prints that it is a str type

#Creating a blank line
print()

#Problem #1 Ask the user for 2 numbers. If number 1 > number 2 ~ print “Number 1 is larger” - Else if number 1 = number 2 ~ print “Numbers are the same” - Else ~ print “Number 1 is smaller”
number1 = int(input("Enter an integer value for number 1"))
number2 = int(input("Enter an integer value for number 2"))

if (number1 > number2):
    print("Number 1 is larger")

elif (number1 == number2):
    print("Numbers are the same")

else:
    print("Number 1 is smaller")

print("\n" + "Program Finished!")