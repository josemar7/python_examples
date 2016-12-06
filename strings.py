import sys

import humansize

s = '深入 Python'
print(len(s))
print(s[0])
print(s + '3')

username = 'mark'
password = 'PapayaWhip'
print("{0}'s password is {1}".format(username, password))

si_suffixes = humansize.SUFFIXES[1000]
print(si_suffixes)
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))

print('1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys))

s = '''Finished files are the re-
    sult of years of scientif-
    ic study combined with the
    experience of years.'''
print(s.splitlines())
print(s.lower())
print(s.lower().count('f'))
query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
print(a_list)
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)

a_string = 'My alphabet starts where your alphabet ends.'
print(a_string[3:11])
print(a_string[3:-3])
print(a_string[0:2])
print(a_string[:18])
print(a_string[18:])

by = b'abcd\x65'
print(by)
print(type(by))
a_string = '深入 Python'
by = a_string.encode('utf-8')
print(by)