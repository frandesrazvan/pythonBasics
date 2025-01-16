# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()

import os

# print(os.getcwd())
# print(os.listdir())
# print(os.listdir('C:\\Users'))

# import shutil

# shutil.move('practice.txt', 'C:\\Users\\RFRANDES\\Downloads\\automation repo\\python\\TheCompletePythonBootcampFromZeroToHeroInPython')
# shutil.move('..\\practice.txt', 'C:\\Users\\RFRANDES\\Downloads\\automation repo\\python\\TheCompletePythonBootcampFromZeroToHeroInPython\\section14')

# Deleting files
'''
os.unlink(path) which deletes a file at the path you provide
os.rmdir(path) which deletes a folder(folder must be empty) at the path you provide
shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders contained in the path

All of these methods can not be reveresed.
Alternative is send2trash module which sends files to recycle bin
'''

# import send2trash

# print(os.listdir())
# send2trash.send2trash('practice.txt')

for folder, sub_folders, files in os.walk(os.getcwd()):
    print(f'Currently looking at {folder}\n')

    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f'Subfolders: {sub_fold}')

    print('\nThe files are: ')
    for f in files:
        print(f'File: {f}')

    print('\n')