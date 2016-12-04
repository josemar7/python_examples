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