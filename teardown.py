import re

# Input File


def tear(tag):
	bra = '\s*' + tag + '[\s\S]*'
	ket = '\s*end ' + tag + '\s*'
	raw_text = open('circle_class.fun')

	comment = '\s*'+'!'+'[\s\S]*'
	count = 0
	split = ''

	for line in raw_text:
		if re.match(comment, line):
			re.sub(comment, 'o', line)
			continue
		if re.match(bra, line):
			count += 1
			continue
		if re.match(ket, line):
			break
		if count > 0:
			split += line

	return split


# tear('test')
# tear('setup')
raw_text = open('circle_class.fun')
for line in raw_text:
	if re.match('(\s*)(test\s+)(\w+)(\s*)', line):
		def changev(matched):
			return matched.group(1) + 'subroutine ' + matched.group(3)
		print re.sub('(\s*)(test\s+)(\w+)(\s*)', changev, line)
