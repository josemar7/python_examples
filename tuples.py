from datatypes import is_it_true

a_tuple = ("a", "b", "mpilgrim", "z", "example")

print(a_tuple)
print(a_tuple[1])
print(a_tuple.index("example"))
print("z" in a_tuple)
is_it_true(())
is_it_true(('a', 'b'))

v = ('a', 2, True)
(x, y, z) = v
print(x + ', ' + str(y) + ', ' + str(z))

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(SATURDAY)