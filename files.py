import glob
import os

import time

print(os.getcwd())
os.chdir(os.getcwd() + '/examples')
print(os.getcwd())
print(os.path)

os.chdir('/home/invitado/PycharmProjects/example/')
print(glob.glob('*.py'))

metadata = os.stat('files.py')
print(metadata)
print(time.localtime(metadata.st_mtime))