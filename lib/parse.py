# -*- coding: utf-8 -*-  
import re, os

class _re(object):

    def __init__(self, matchstring):
        self.matchstring = matchstring

    def match(self,regexp):
        self.rematch = re.match(regexp, self.matchstring)
        return bool(self.rematch)

    def group(self,i):
        return self.rematch.group(i)



class Parse(object):
    
    def __init__(self, raw_text):
        self.raw = raw_text
        self.ripe = raw_text + '.f90'
        self.text = open(raw_text)
        self.target = open('TestRunner.f90', 'w')


    def __del__(self):
        self.text.close()
        self.target.close()



    def render(self):
        comment = '\s*'+'!'+'[\s\S]*'
        bone = ''

        for line in self.text:
            m = _re(line)
            if m.match('\s*subroutine\s+setup\s*'):
                continue
            if m.match('\s*subroutine\s+teardown'):
                continue
            if m.match('(\s*)(subroutine)(\s+\w+\s*)'):
                bone += '\tcall setup\n'
                bone += m.group(1) + 'call' + m.group(3)
                bone += '\tcall teardown\n'
                continue
        return bone


    def header(self):

        for line in self.text:
            m = _re(line)
            if m.match('(\s*module\s+)(\w+)(\s*)'):
                _mod = m.group(2)
                break

        header1 = '''program main\n'''
        header2 = '''\tuse %s\n''' % _mod
        header3 = '''\timplicit none\n'''
        return header1 + header2 + header3



    def footer(self):
        return '''end program'''



    def write_to_target(self):
        self.target.write(self.header())
        self.target.write(self.render())
        self.target.write(self.footer())

        cmd = 'cp %s %s' % (self.raw, self.ripe)
        os.system(cmd)


    