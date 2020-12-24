myfile = open('text.txt')

print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()

with open('text.txt') as my_new_file:
    contents = my_new_file.read()
    
print('Content is', contents)

with open('text.txt', mode='a') as my_new_file:
    my_new_file.write('\noutra linha')

with open('text.txt',mode='r') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('newfile.txt',mode='w') as new_file:
    new_file.write('created that file')