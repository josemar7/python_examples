from datatypes import is_it_true

a_list = ['a', 'b', 'mpilgrim', 'z', 'example']

print(a_list)
print(a_list[-1])
print(a_list[1])
print(a_list[1:3])

a_list = a_list + [2.0, 3]
a_list.append(True)
a_list.extend(['four', 'Ω'])
print(a_list)
a_list.insert(0, '¿?')
print(a_list)
print(len(a_list))
print(a_list.count('four'))
print('b' in a_list)
print(a_list.index('mpilgrim'))
try:
    print(a_list.index('mpilgrim111'))
except:
    print('value not found')
del a_list[10]
print(a_list)
a_list.remove('four')
print(a_list)
print(a_list.pop())
print(a_list)

is_it_true([])
is_it_true([False])