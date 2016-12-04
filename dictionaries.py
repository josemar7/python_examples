import glob
import os

import humansize
from humansize import SUFFIXES

a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict['server'])
try:
    print(a_dict['db.diveintopython3.org'])
except KeyError:
    print('element is not in the dictionary')
print(a_dict['database'])
print(len(SUFFIXES))
print(SUFFIXES[1024][4])

metadata = [(f, os.stat(f)) for f in glob.glob('*.py')]
print(metadata[0])
metadata_dict = {f:os.stat(f) for f in glob.glob('*.py')}
print(type(metadata_dict))
print(list(metadata_dict.keys()))
print(metadata_dict['tuples.py'].st_size)
metadata_dict = {f:os.stat(f) for f in glob.glob('*')}
print(metadata_dict)
humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size) \
    for f, meta in metadata_dict.items() if meta.st_size > 500}
print(humansize_dict)
a_dict = {'a': 1, 'b': 2, 'c': 3}
print({value:key for key, value in a_dict.items()})
a_dict = {'a': [1, 2, 3], 'b': 4, 'c': 5}
try:
    print({value:key for key, value in a_dict.items()})
except TypeError:
    print('error!!!')