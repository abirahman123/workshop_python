#Numbers

a = 2 + 2

b = 50 - 5*6

c = (50 - 5*6) / 4

d = 8 / 5  # division always returns a floating point number

print (a)
print (b)
print (c)
print (d)
print("=========================")

e = 17 / 3  # classic division returns a float

f= 17 // 3  # floor division discards the fractional part

g = 17 % 3  # the % operator returns the remainder of the division

h = 5 * 3 + 2  # floored quotient * divisor + remainder

print (e)
print (f)
print (g)
print (h)
print("=========================")

i = 5 ** 2  # 5 squared

j = 2 ** 7  # 2 to the power of 7

print(i)
print(j)
print("=========================")

width = 20
height = 5 * 9
wide = width * height

print("wide: ", wide)
print("=========================")

k = 4 * 3.75 - 1
print(k)
print("=========================")

tax = 12.5 / 100
price = 100.50
cost = price * tax
cost2 = price + cost
round(cost2,2)
print("cost: ",cost)
print("cost2: ",cost2)
print("round: ",round(cost2, 2))
print("=========================")


#String
A = 'spam eggs' #single quotes
B = 'doesn\'t'  #use \' to escape the single quote...
C = "doesn't"   #...or use double quotes instead
D = '"Yes," they said.'
E = "\"Yes,\" they said."
F = '"Isn\'t," they said.'

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print("=========================")

'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)  # with print(), \n produces a new line First line.
print("=========================")

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote
print("=========================")

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print("=========================")

# 3 times 'un', followed by 'ium'
word = 3 * 'un' + 'ium'
print(word)
print("=========================")

word2 = 'Py' 'thon'
print(word2)
print("=========================")

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print("=========================")

prefix = 'Py'
print(prefix + 'thon')
print("=========================")

word3 = 'python'
print(word3[0])   #character in position 0
print(word3[5])   #character in position 5
print(word3[-1])  #Last character
print(word3[-2])  # Second-last character
print(word3[-6])
print("=========================")

print(word3[0:2])  #characters from position 0 (included) to 2 (excluded)
print(word3[2:5])  #characters from position 2 (included) to 5 (excluded)
print("=========================")

print(word3[:2])   # character from the beginning to position 2 (excluded)
print(word3[4:])   # characters from position 4 (included) to the end
print(word3[-2:])  # characters from the second-last (included) to the end
print("=========================")

print(word3[:2] + word3[2:])
print(word3[:4] + word3[4:])
print("=========================")

print(word3[4:42])
print(word3[42:])
print("=========================")

print('J' + word3[1:])
print(word3[:2] + 'py')
print("=========================")

s = 'supercalifragilisticexpialidocious'
print(len(s))
print("=========================")

#List
squares = [1, 4, 9, 16, 25]
print(squares)
print("=========================")

print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list
print("=========================")

print(squares[:])
print(squares + [36, 49, 64, 81, 100])
print("=========================")

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print(4 ** 3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print(cubes)
print("=========================")

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
print("=========================")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)
print("=========================")

Letters = ['a', 'b', 'c', 'd']
print(len(Letters))
print("=========================")

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
print("=========================")

#First steps towards programing
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
print("=========================")

i = 256*256
print('The value of i is', i)
print("=========================")

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
print("=========================")