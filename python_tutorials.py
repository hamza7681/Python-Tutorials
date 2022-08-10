# list comprehension
l = []
for a in range(1, 101):
    l.append(a)
print(l)

# CRUD operations on list
lists = [10, 20, 30, 40, 50]
del lists[2]
print(lists)
print(lists.pop(0))
lists.remove(50)
print(lists)
lists.clear()
print(lists)
lists.insert(0, 10)
print(lists)
lists.append(70)
print(lists)
list2 = [10, 20]
lists.extend(list2)
print(lists)

# list functions
print(lists.count(10))
print(max(lists))
print(min(lists))
lists.sort()
print(lists)
lists.reverse()
print(lists)
print(lists.index(10))

# zip function
l1 = [10, 20, 30, 40]
l2 = [3, 4, 55, 66]
for a, b in zip(l1, l2):
    print(a, b)

# convert string to list
# n = input('Enter the value: ')
# print(n)
# l = n.split()
# print(l)
# newList = []
# for a in range(1, 4):
#     n = input('Enter the value number'+str(a)+": ")
#     newList.append(n)
# print(newList)

person = {
    "name": "Hamza Siddique",
    "age": 24,
    "class": "BSCS"
 }

for a in person:
    print(a, person[a])
print(person.get('name'))
for a in person.keys():
    print(a)
for a in person.values():
    print(a)
for a, b in person.items():
    print(a, b)
del person['class']
print(person)
a = person.pop('age')
print(a)

# nested dictionary

course = {
    "Python": {"title": "Python", "duration": "2 Months"},
    "React": {"title": "React", "duration": "3 Months"},
}
print(course)
for a in course:
    print(course[a]['duration'])

# Tuples
t = (10, 20, 30, 50, 40)
print(t[2])
print(len(t))
for a in t:
    print(a)
print(min(t))
print(max(t))
print(t.count(50))
print(t.index(40))
print(sum(t))