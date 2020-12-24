mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)

my_string = 'Hello World'

for letter in my_string:
    print(letter)

tup = (1,2,3)

for t in tup:
    print(t)

my_list = [(1,2), (3,4),(5,6),(7,8)]

for a,b in my_list:
    print(a)
    print(b)

d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(value)

for value in d.values():
    print(value)

x = [1,2,3]

for i in x:
    if i == 1:
        pass
    elif i == 2:
        print(f'This is {i}')
    else:
        break