__author__ = 'Gabriel Araujo'

tokens_01 = [
    ('IF', ), ('ID', 'x'), ('COLON', ), ('BEGIN', ), ('PASS', ), #('END', )
]

data_01 = '''
if x :
    pass'''

tokens_02 = [
    ('IF', ), ('ID', 'test'), ('COLON', ), ('BEGIN', ), ('PASS', ), ('END', ), ('ELSE', ), ('COLON', ), ('BEGIN', ),
    ('ID', 'fail'), #('END', ),
]

data_02 = '''
if      test:
    pass
else:
    fail
    '''
