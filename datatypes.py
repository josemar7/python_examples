import fractions

import math

size = 1
print(size < 0)
print(True + True)
print(True * True)
print(type(1))
print(type(2.0))
print(float(2))
print(int(2.5))

print(11 // 2)
print(11 ** 2)
print(11 % 2)

x = fractions.Fraction(1, 3)
print(x + x)
print(math.sin(math.pi / 2))

def is_it_true(anything):
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")

is_it_true(1)
is_it_true(0)
