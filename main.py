print('Hello World')
print(20+30)
# variables

a = 10
b = 'Hamza'
print(a)
print(b)
# find the location of variable in memory
print(id(a))

# concatenation of string
c = "Hamza"
d = "Siddique"
print(c+' '+d)

# arithematic operators

e = 10
f = 20
print(e+f)
print(e-f)
print(e/f)
print(e*f)
print(e**f)
print(e//f)
print(e % f)

# assignment operators
x = 3
print(x)
x += 3
print(x)
x -= 3
print(x)

# comparison operators
num1 = 10
num2 = 20

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 <= num2)
print(num1 >= num2)

# logical operators
print(num1 < num2 and num1 == num2)
print(num1 > num2 or num1 == num2)
print(not(num1 < num2))

# membership operators
string = 'Hamza'
print('H' in string)
print('a' not in string)

# identity operators
string2 = 'Hamza'
print(string2 is string)
print(string2 is not string)

# bitwise operators
s = 10
m = 20
o = 3.2
print(bin(s), bin(m))
print(s & m)
print(s | m)
print(s ^ m)

# Datatypes
# Mutable list, dictionary, byte array
# Immutable int, float, complex, string, tuple, set

comp = 2+3j
print(s, type(s))
print(o, type(o))
print(comp, type(comp))
multi = '''This is
good practice
'''
print(multi, type(multi))
listing = [1, 2, 'w', 4]
listing[2] = 'h'
print(listing, type(listing))
t = (1, 2, 'r', 6)
print(t, type(t))
person = {
    "name": "Hamza",
    "age": 24
}
print(person, type(person))
my_set = {1, 2, 3, 2}
print(my_set, type(my_set))

# User input and Type Casting
# user1 = input('Enter first number: ')
# user2 = input('Enter second number: ')
# print(int(user1)+int(user2))
# print(eval(user1)+eval(user2))

# conditional Statements
even = 9
if even % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')

marks = 78
if marks >= 80:
    print('A Grade')
elif marks >= 70:
    print('B Grade')
else:
    print('Fail')

# For Loop with Range()
# range(5)
# start=0, condition<5, increment=1
# range(1, 6)
# start=1, condition<6, increment=1
# range(1, 6, 2)
# start=1, condition<6, increment=2
for n in range(5):
    print(n)

# while loop
i = 1
while i <= 5:
    print('Hamza')
    i = i+1

# string indexing and Split String
msg = "python tutorials 2"
print(msg[7])
# last character
print(msg[-1])
# slice
print(msg[0:6])

# string Iteration
print(len(msg))
for a in msg:
    print(a)

# string functions
lower = msg.lower()
upper = msg.upper()
title = msg.title()
cap = msg.capitalize()
print(lower)
print(upper)
print(title)
print(cap)
print(msg.find('t'))
print(msg.index('y'))
print(msg.isalpha())
print(msg.isalnum())
print(msg.isdigit())

# python chr() and ord()
y = chr(65) # from ASCII to character
print(y)
z = ord('A') # from character to ASCII
print(z)

# String Format
txt = "Welcome {fname}".format(fname='Hamza')
print(txt)

# create List
newList = [1, 2, 3, [1, 2, 3]]
print(newList[3][1])
listings = [1, 2, 3, 4, 5]
length = len(listings)
for n in range(length):
    print(length[n])

# list comprehension in python
array = []
for a in range(1, 101):
    array.append(a)
print("array")