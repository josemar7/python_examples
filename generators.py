import itertools

unique_characters = {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
gen = (ord(c) for c in unique_characters)
print(gen)
print(next(gen))
print(next(gen))
print(tuple(ord(c) for c in unique_characters))

def ord_map(a_string):
    for c in a_string:
        yield ord(c)

gen = ord_map(unique_characters)
print(gen)
print(next(gen))
print(next(gen))

perms = itertools.permutations([1, 2, 3], 2)
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
# print(next(perms))

perms = itertools.permutations('ABC', 3)
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
print(next(perms))
print(list(itertools.permutations('ABC', 3)))

print(list(itertools.product('ABC', '123')))
print(list(itertools.combinations('ABC', 2)))

names = list(open('examples/favorite-people.txt', encoding='utf-8'))
print(names)
names = [name.rstrip() for name in names]
print(names)
names = sorted(names)
print(names)
names = sorted(names, key=len)
print(names)
groups = itertools.groupby(names, len)
print(groups)
print(list(groups))
groups = itertools.groupby(names, len)
for name_length, name_iter in groups:
    print('Names with {0:d} letters:'.format(name_length))
    for name in name_iter:
        print(name)

print(list(range(0, 3)))
print(list(range(10, 13)))
print(list(itertools.chain(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 13))))
print(list(zip(range(0, 3), range(10, 14))))
print(list(itertools.zip_longest(range(0, 3), range(10, 14))))

characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
guess = ('1', '2', '0', '3', '4', '5', '6', '7')
print(tuple(zip(characters, guess)))
print(dict(zip(characters, guess)))