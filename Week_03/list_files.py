import os

print('The files and folders in {} are:'.format(os.getcwd()))
items = os.listdir('../Tests')
for item in items:
    print(item)
