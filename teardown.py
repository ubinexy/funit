import re

# Input File
raw_text = open('gen.f90')
# keyword for matching
bra = '\s*setup\s*'
ket = '\s*end\s+setup\s*'
# iretator
count = 0
split = ''

for line in raw_text:
	if re.match('\s*!*', line)
		continue

	if re.match(bra, line):
		count += 1
		continue

	if re.match(ket, line):
		count -= 1
		continue

	if count > 0:
		split += line

print split 