import re

s = '100 NORTH MAIN ROAD'
print(s.replace('ROAD', 'RD.'))
s = '100 NORTH BROAD ROAD'
print(s.replace('ROAD', 'RD.'))
print(s[:-4] + s[-4:].replace('ROAD', 'RD.'))
print(re.sub('ROAD$', 'RD.', s))

s = '100 BROAD'
print(re.sub('ROAD$', 'RD.', s))
print(re.sub('\\bROAD$', 'RD.', s))
s = '100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD$', 'RD.', s))
print(re.sub(r'\bROAD\b', 'RD.', s))

pattern = '^M?M?M?$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MM'))
print(print(re.search(pattern, 'MMM')))
print(print(re.search(pattern, 'MMMM')))
print(print(re.search(pattern, '')))

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print(re.search(pattern, 'MCM'))
print(re.search(pattern, 'MD'))
print(re.search(pattern, 'MMMCCC'))
print(re.search(pattern, 'MCMC'))
print(re.search(pattern, ''))

pattern = '^M{0,3}$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MMMM'))

pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
print(re.search(pattern, 'MCMXL'))
print(re.search(pattern, 'MCML'))
print(re.search(pattern, 'MCMLX'))
print(re.search(pattern, 'MCMLXXX'))
print(re.search(pattern, 'MCMLXXXX'))

pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print(re.search(pattern, 'MDLV'))
print(re.search(pattern, 'MMDCLXVI'))
print(re.search(pattern, 'MMMDCCCLXXXVIII'))
print(re.search(pattern, 'I'))

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('800-555-1212-1234'))
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('800 555 1212 1234'))
print(phonePattern.search('800-555-1212'))
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('80055512121234'))
print(phonePattern.search('800-555-1212'))
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('(800)5551212 x1234'))