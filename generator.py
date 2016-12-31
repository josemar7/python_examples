from closures import build_match_and_apply_functions


def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x = x + 1

counter = make_counter(1)
print(counter)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

for n in fib(1000):
    print(n, end=' ')

def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)


def plural(noun, rules_filename='plural4-rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))
print()
print(plural('josef'))