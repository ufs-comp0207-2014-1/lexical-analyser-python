# ------------------------------------------------------------
# tinypylex.py
#
# tokenizer for TinyPy language
# ------------------------------------------------------------
__author__ = 'Gabriel Araujo'

import ply.lex as lex

# Levels of indentation
# Start with level 0, where the size of space is 0.
levels = [0]

# List of reserved words
reserved = (
    'IF', 'ELSE', 'PASS'
)

# String match for reserved words
reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

# List of token names.   This is always required
tokens = reserved + (

    # Literals (identifier, integer constant)
    'ID', #'ICONST',

    # Indentation tokens
    'BEGIN', 'END',

    # Delimeters ( ) :
    'LPAREN', 'RPAREN', 'COLON',
)

# Delimiters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_COLON            = r':'


# Identifiers and reserved words
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

# Error handling rule
def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

##############################################

# Test it out
data = '''
if x :
    pass
else:
    pass
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)