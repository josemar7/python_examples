from datatypes import is_it_true

a_set = {1, 2}
a_list = ['a', 'b', 'mpilgrim', True, False, 42]

print(a_set)
print(type(a_set))
a_set = set(a_list)
print(a_set)
print(a_list)

a_set = set()
print(a_set)
print(len(a_set))
not_sure = {}
print(type(not_sure))
a_set.add(4)
print(a_set)
a_set.update({2, 4, 6})
print(a_set)
a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
print(a_set)
a_set.discard(5)
print(a_set)
a_set.remove(4)
print(a_set)
print(a_set.pop())
print(a_set)
a_set.clear()
print(a_set)
try:
    print(a_set.pop())
except KeyError:
    print('set is empty')

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
print(a_set.union(b_set))
print(8 in a_set.union(b_set))
is_it_true(set())
is_it_true(set({False}))

a_set = set(range(10))
print(a_set)
print({x ** 2 for x in a_set})
print({x for x in a_set if x % 2 == 0})
print({2**x for x in range(10)})

a_list = ['The', 'sixth', 'sick', "sheik's", 'sixth', "sheep's", 'sick']
print(set(a_list))
a_string = 'EAST IS EAST'
print(set(a_string))
words = ['SEND', 'MORE', 'MONEY']
print(''.join(words))
print(set(''.join(words)))