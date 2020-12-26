mystring = 'Hello'

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

mylist = [letter for letter in mystring]

print(mylist)

mylist2 = [x**2 for x in range(0,11)]

print(mylist2)

mylist3 = [i**2 for i in range(0,11) if i%2==0]

print(mylist3)

celsius = [0,10,20,34.5]

fahrenheit = [((9/5)*temp+32) for temp in celsius]

print(fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]

print(results)

results = [x for x in range(0,11) if x%2==0]

print(results)

mylist = [x*y for x in [2,4,6] for y in [1,10,100]]

print(mylist)