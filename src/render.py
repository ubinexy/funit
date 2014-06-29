# -*- coding: utf-8 -*-  

import re
raw_text = open('circle_class.fun')

def header():
    header1 = '''program main\n''' 
    header2 = cutup('module','contains')
    setup_doc = cutup('setup', 'end setup')
    return header1 + header2 + setup_doc



def footer():
    teardown_doc = cutup('teardown', 'end teardown')
    return teardown_doc + '''end program'''

def render():
    count = 0
    split1 = ''
    split2 = ''

    def change1(matched):
        return matched.group(1) + 'subroutine ' + matched.group(3) 

    def change2(matched):
        return matched.group(1) + 'call ' + matched.group(3)

    for line in raw_text:
        if re.match('(\s*)(test\s+)(\w+\s*)', line):
            count += 1
            name1 = re.sub('(\s*)(test\s+)(\w+\s*)', change1, line)
            name2 = re.sub('(\s*)(test\s+)(\w+\s*)', change2, line)
            split1 += name1
            split2 += name2
            continue
        if re.match('\s*end test\s*', line):
            split1 += re.sub('(\s*end )(test)(\s*)', change1, line) + '\n'
            count -= 1
            continue
        if count > 0:
            split1 += line
        else:
            pass

    # split += name2
    return (split2, split1)



def cutup(tag, _tag):
    bra = '\s*' + tag + '[\s\S]*'
    ket = '\s*' + _tag + '[\s\S]*'

    comment = '\s*'+'!'+'[\s\S]*'
    count = 0
    split = ''

    for line in raw_text:
        if re.match(comment, line):
            continue
        if re.match(bra, line):
            count += 1
            continue
        if re.match(ket, line):
            break
        if count > 0:
            split += line
    return split



# ヽ(# ≧Д≦)ノ

print header()
raw_text = open('circle_class.fun')
raw_tt = raw_text.read()
raw_text = open('circle_class.fun')

# temp =  raw_tt.count('end test')
a = render()
# for i in range(temp):
print a[0]
print footer()
print a[1]
