# Simple print
print('Hello World!')

# mod
print(7 % 4)

# power
print(2 ** 3)

a = 10

print(a)

print(type(a))
print(len('test'))

test = 'abcdefghijk'

print(test[2])

print(test[-1])

print(test[2:])

print(test[::2])
print(test[2:7:2])

print('tinker'[1:4])

print(test.upper())

print('This is a string {}'.format('INSERTED'))

print('The {} {} {} '.format('fox', 'brown','quick'))

print('The {2} {1} {0} '.format('fox', 'brown','quick'))

# print('The {0} {0} {0} '.format('fox', 'brown','quick'))

print('The {q} {b} {f} '.format(f='fox', b='brown',q='quick'))

# Formating number with precision
result = 100/777

print("The result was {r:5.3f}".format(r=result))

name = 'Jose'

print('Hello, his name is {}'.format(name))

print(f'Hello, his name is {name}')

age = 30

print(f'{name} is {age} years old.')

print('Python {}'.format('rules'))

def myfunc(str):
    
    mystr = ''
    counter = 1
    
    for letter in str:
        if counter % 2 == 0:
            print('counter even')
            mystr = mystr + letter.upper()
        else:
            print('counter odd')
            mystr = mystr + letter.lower()
        counter=counter+1
        
    return mystr

result4 = myfunc('Erick')

print(result4)