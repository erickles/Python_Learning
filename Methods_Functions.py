# def say_hello():
#     print('hello')

# say_hello()

def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello('Erick')

def sum_number (num1, num2):
    return num1+num2

result = sum_number(10,20)

print(result)

def even_check(num):
    return num % 2 == 0

print(even_check(97))

# Returning Tuples

work_hours  = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if current_max < hours:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)

print(employee_check(work_hours))

def shuffle_list(list):
    from random import shuffle
    shuffle(list)
    return list

result = shuffle_list([1,2,3])

print(result)

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input('Pick a number> 0, 1 or 2:')

    return int(guess)

# player_guess()

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print('mylist')

# Initial guess
mylist = ['','O','']

# Shuffle List
mixedup_list = shuffle_list(mylist)

# User guess
guess = player_guess()

# Check guess
check_guess(mixedup_list,guess)