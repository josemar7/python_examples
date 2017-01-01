class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

class Test:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.c = 0
        return self

    def __next__(self):
        c = self.c
        if c > self.max:
            raise StopIteration
        self.c = self.c + 1
        return  c

fib = Fib(100)
print(fib)
print(fib.__class__)
print(fib.__doc__)
fib1 = Fib(100)
fib2 = Fib(200)
print(fib1.max)
print(fib2.max)

for n in Fib(1000):
    print(n, end=' ')

print()
for n in Test(50):
    print(n, end=' ')