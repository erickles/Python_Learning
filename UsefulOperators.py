for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

for num in range(0,10,2):
    print(num)

# Casting into a list

print(list(range(0,10,2)))

index_count = 0

word = 'abcde'

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1,mylist2):
    print(item)

print('x' in [1,2,3])

print('a' in 'a world')

d = {'mykey':345}

print('mykey' in d)

print(345 in d.values())

print(345 in d.keys())

numberlist = [10,20,30,40,50,60,70,80,90,100]

print(min(numberlist))

print(max(numberlist))

from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

from random import randint

print(randint(0,100))

result = input('Enter a number here:')

print(float(result))
