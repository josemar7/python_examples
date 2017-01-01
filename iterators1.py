import re

from closures import build_match_and_apply_functions


class LazyRules:
    rules_filename = 'plural4-rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0
        return self

    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(
            pattern, search, replace)
        self.cache.append(funcs)
        return funcs

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

rules = LazyRules()
print(rules)
r1 = LazyRules()
r2 = LazyRules()
print(r1.rules_filename)
print(r2.rules_filename)
r2.rules_filename = 'r2-override.txt'
print(r1.rules_filename)
print(r2.rules_filename)
print(r2.__class__.rules_filename)
r2.__class__.rules_filename = 'papayawhip.txt'
print(r1.rules_filename)
print(r2.rules_filename)
print(plural('franciscox'))