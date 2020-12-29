
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('TypeError! Watch out!')

try:
    x = 5
    y = 0
    z = x/y
except:
    print('Error!!')
finally:
    print('All Done')

def ask():
    while True:
        try:
            n = int(input('Enter a number'))
        except:
            print('Please try again! \n')
            continue
        else:
            break
    print(n**2)

ask()