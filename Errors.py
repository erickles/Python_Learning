def add(n1,n2):
    print(n1+n2)

add(1,2)

try:
    # Want to attempt this code
    # May have an error
    result = 10 + 10
except:
    print("Hey it looks like you aren´t adding correctly!")
else:
    print('Add went well!')
    print(result)

try:
    f = open('testfile.txt','w')
    f.write('Write a test line')
# except TypeError:
#     print('There was a type error!')
# except OSError:
#     print('Hey you have an OS Error')
except:
    print('All other exceptions!')
finally:
    print('I always run')

def ask_for_int():
    while True:

        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print("End of try/except/finally")
            print('I always run at the end!')

ask_for_int()


