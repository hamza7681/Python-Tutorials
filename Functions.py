import Module1
from Module1 import Multiply
import math
import random
import datetime
import pickle
import json

# sets
# sets are un-order, un-index
# no element repeat
s = {10, 20, 30}
for a in s:
    print(a)
l = [10, 20, 30]
s = set(l)
print(s)
s.add(40)
print(s)
s.pop()
print(s)
s.remove(20)
print(s)
s.clear()
print(s)
newSet = {10, 20, 30}
list = [40, 60]
newSet.update(list)
print(newSet)

# Functions
def welcome():
    print('Hello Python')

welcome()

def sum(a, b):
    print(a * b)

sum(2, 3)

def substract(a, b):
    c = a - b
    return c
res = substract(20, 10)
print(res)

# modules
print(Module1.SumData(10, 20))
print(Multiply(10, 20))

# Math Modules
x = 10.5
y = -10.6
f = 5
print(math.ceil(x))
print(math.fabs(x))
print(math.factorial(f))
print(math.floor(x))

# Random Modules
print(random.randint(5, 10))
print(random.randrange(3, 9))
choiceList = ['muaz', 'talha', 'ibrahim']
print(random.choice(choiceList))
# dateTime
time = datetime.datetime.now()
print(time)
month = time.strftime("%b")
print(month)
month_num = time.strftime("%m")
print(month_num)

# pickel module
# dump() -> serialize a object heirarchy
# load() -> de-serialize a data stream
example = {
    1: "6",
    2: "7",
    3: "F"
}
file = open('writedata.txt', 'wb')
pickle.dump(example, file)
file.close()
openFile = open('writedata.txt', 'rb')
newfile = pickle.load(openFile)
print(newfile)

# JSON in python
jsonFile = {
    "name": "Hamza Mughal",
    "age": 24,
    "class": "BSCS"
}
f = json.dumps(jsonFile)
print(f, type(f))
newF = json.loads(f)
print(newF, type(newF))
openNewFile = open('data.json', 'r')
m = openNewFile.read()
finalData = json.loads(m)
for a in finalData:
    print(a)

