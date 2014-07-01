# -*- coding: utf-8 -*-  
import re

class Finding(object):

    def __init__(self, raw_text):
        self.text = open(raw_text)


    def __del__(self):
        self.text.close()


    def cut_out(self, tag, _tag):

        bra = '\s*' + tag + '[\s\S]*'
        ket = '\s*' + _tag + '[\s\S]*'

        comment = '\s*'+'!'+'[\s\S]*'
        count = 0
        cuts = ''

        for line in self.text:
            if re.match(comment, line):
                continue
            if re.match(bra, line):
                count += 1
                continue
            if re.match(ket, line):
                break
            if count > 0:
                cuts += line
        
        return cuts



    def render(self):

        bra = '(\s*)(test\s+)(\w+\s*)'
        ket = '(\s*end\s+)(test)(\s*)'

        comment = '\s*'+'!'+'[\s\S]*'
        count = 0
        skin = ''
        bone = ''

        def substitute1(matched):
            return matched.group(1) + 'subroutine ' + matched.group(3) 

        def substitute2(matched):
            return matched.group(1) + 'call ' + matched.group(3)

        for line in self.text:
            if re.match(comment, line):
                continue
            if re.match('\s*test\s+\w+\s*', line):
                count += 1
                name1 = re.sub(bra, substitute1, line)
                name2 = re.sub(bra, substitute2, line)
                bone += name1
                skin += name2
                continue
            if re.match('\s*end\s+test\s*', line):
                bone += re.sub(ket, substitute1, line) + '\n'
                count -= 1
                continue
            if count > 0:
                bone += line

        return (skin, bone)



class Rendering(Finding):

    def __init__(self, raw_text, arg1):
        super(Rendering, self).__init__(raw_text)
        self.target = open(arg1, 'w')



    def __del__(self):
        super(Rendering, self).__del__()
        self.target.close()



    def cut_out(self, tag, _tag):
        return super(Rendering, self).cut_out(tag, _tag)


    def render(self):
        return super(Rendering, self).render()


    def header(self):
        header1 = '''program main\n''' 
        header2 = self.cut_out('module','contains')
        setup_doc = self.cut_out('setup', 'end setup')
        return header1 + header2 + setup_doc    



    def footer(self):
        teardown_doc = self.cut_out('teardown', 'end teardown')
        return teardown_doc + '''end program\n'''



    def write_to_target(self):
        self.target.write(self.header())
        a = self.render()
        self.target.write(a[0])
        self.target.write(self.footer())
        self.target.write(a[1])



# ヽ(# ≧Д≦)ノ
b = Rendering('circle_class.fun', 'main.f90')
b.write_to_target()

    