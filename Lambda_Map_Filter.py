def square(num):
    return num**2

my_nums = [1,2,3,4,5,6]

for item in map(square,my_nums):
    print(item)

def check_even(num):
    return num % 2 == 0

for item in filter(check_even, my_nums):
    print(item)

square = lambda num: num ** 2

print(square(3))

my_list = list(map(lambda num: num**2,my_nums))

print(my_list)

my_list = list(filter(lambda num: num % 2 == 0, my_nums))

print(my_list)
