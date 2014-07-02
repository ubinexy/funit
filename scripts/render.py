# -*- coding: utf-8 -*-  
import re, os

class Finding(object):

    def __init__(self, file):
        # file += '.fun'
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



class Rendering(Finding):
    '''
    before
    $(PRO_DIR)/tests/class.test
    after:
    $(PRO_DIR)/tests/class_test.f90
    TestRunner.f90
    '''
    def __init__(self, raw_text, ripe_text):
        self.dir = '/Users/shiqi/Projects/funit/' + 'tests/'
        self.raw = raw_text + '.test'
        self.ripe = ripe_text
        # self.raw = self.dir + raw_text + '_test.f90'
        super(Rendering, self).__init__( self.dir + self.raw )
        self.target = open('TestRunner.f90', 'w')



    def __del__(self):
        super(Rendering, self).__del__()
        self.target.close()



    def render(self):
        return super(Rendering, self).render()


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

        cmd = 'cp %s %s.f90' % (self.dir + self.raw, self.dir + self.ripe)
        os.system(cmd)

# ヽ(# ≧Д≦)ノ

# b = Rendering('circle_class', 'circle_class_test')
# b.write_to_target()

    