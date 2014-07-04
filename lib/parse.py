# -*- coding: utf-8 -*-  
import re, os

class Find(object):

    def __init__(self, file):
        self.text = open(file)


    def __del__(self):
        self.text.close()


    def render(self):

        bra = '(\s*)(subroutine\s+)(\w+\s*)'

        comment = '\s*'+'!'+'[\s\S]*'
        count = 0
        bone = ''

        def substitute(matched):
            return matched.group(1) + 'call ' + matched.group(3) 

        for line in self.text:
            if re.match('\s*subroutine\s+setup\s*', line):
                continue
            if re.match('\s*subroutine\s+teardown', line):
                continue
            if re.match('\s*subroutine\s+\w+\s*', line):
                bone += '\tcall setup\n'
                bone += re.sub(bra, substitute, line)
                bone += '\tcall teardown\n'                
                continue
            if count > 0:
                bone += line
        return bone



class Parse(Find):
    
    def __init__(self, raw_text):
        
        Find.__init__( self, raw_text)
        self.raw = raw_text
        self.ripe = raw_text + '.f90'
        self.target = open('TestRunner.f90', 'w')



    def __del__(self):
        Find.__del__(self)
        self.target.close()



    def render(self):
        return Find.render(self)


    def header(self):
        header1 = '''program main\n'''
        header2 = '''\tuse assert_class\n'''
        header3 = '''\tuse circle_class\n'''
        header4 = '''\tuse %s\n''' % self.ripe
        header5 = '''\timplicit none\n'''
        return header1 + header2 + header3 + header4 + header5



    def footer(self):
        return '''end program'''



    def write_to_target(self):
        self.target.write(self.header())
        self.target.write(self.render())
        self.target.write(self.footer())

        cmd = 'cp %s %s' % (self.raw, self.ripe)
        os.system(cmd)

# ヽ(# ≧Д≦)ノ

# b = Rendering('circle_class', 'circle_class_test')
# b.write_to_target()

    