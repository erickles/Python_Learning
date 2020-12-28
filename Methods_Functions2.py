# *args, I can receive as many arguments I want

def myfunc(*args):
    return sum(args) * 0.05

result = myfunc(1,2,3,4,5)

print(result)

# **kwargs, you can receive multiple dictionaries at once
def myfunc2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc2(fruit='Mango', veggie='Lettuce')

def myfunc3(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc3(1,2,3,4,5,fruit='Mango', food='Chicken')

x = 50

def myfunc4():
    global x
    print(f'X is {x}')

    x = 'NEW VALUE'
    print(f'I just locally changed global x to {x}')

myfunc4()

print(x)