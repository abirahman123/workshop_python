#MORE ON LIST
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting at position 4
print(" ")

fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())
print("  ")

#USING LIST AS A STACK
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)
print(" ")

#USING LIST AS A QUEUES
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())          # The first to arrive now leaves
print(queue.popleft())          # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival
print(" ")

#LIST COMPREHENSIONS
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)
print(" ")

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# the tuple must be parenthesized, otherwise an error is raised
# print([x, x**2 for x in range(6)])
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
print(" ")

#List comprehensions can contain complex expressions and nested functions:
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
print(" ")

#Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#The following list comprehension will transpose rows and columns:
print([[row[i] for row in matrix] for i in range(4)])

#As we saw in the previous section, the inner list comprehension is 
# evaluated in the context of the for that follows it, so this example is equivalent to:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
#which, in turn, is the same as:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

#In the real world, you should prefer built-in functions to complex flow 
# statements. The zip() function would do a great job for this use case:
print(list(zip(*matrix)))
print(" ")

#THE DEL STATEMENT
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
print(" ")

#del can also be used to delete entire variables:
del a

#TUPLES AND SEQUENCES
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable:
#print(t[0] = 88888)

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)
print(" ")

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)
print(" ")

#The statement t = 12345, 54321, 'hello!' is an example of tuple packing: the values 12345,
#54321 and 'hello!' are packed together in a tuple. The reverse operation is also possible:
x, y, z = t

#SETS
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)               # show that duplicates have been removed
print('orange' in basket)                 # fast membership testing
print('crabgrass' in basket)
print(" ")

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(a -b)                               # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both
print(" ")

#Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(" ")

#DICTIONARIES
#Here is a small example using a dictionary:
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)
print(" ")

#The dict() constructor builds dictionaries directly from sequences of key-value pairs:
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

#In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
print({x: x**2 for x in (2, 4, 6)})

#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
print(dict(sape=4139, guido=4127, jack=4098)),
print(" ")

#LOOPING TECHNIQUES
#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
print(" ")

#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v),
print(" ")

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a)),
print(" ")

#To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i),
print(" ")

#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i),
print(" ")

#Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence 
# is an idiomatic way to loop over unique elements of the sequence in sorted order.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f),
print(" ")

#It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
print(" ")

#More on Conditions
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)