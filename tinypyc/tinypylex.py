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
    'INDENT', 'BEGIN', 'END',

    # Delimeters ( ) :
    'LPAREN', 'RPAREN', 'COLON',
)

# Delimiters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_COLON            = r':'

# Completely ignored characters
t_ignore           = ' '

# Identifiers and reserved words
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

def t_INDENT(t):
    r'\n[ ]*.'
    level = len(t.value) - 2
    # current level
    curr = levels[-1]
    if level > curr :
        levels.append(level)
        t.type = 'BEGIN'
        t.lexer.lexpos -= 1;
    elif level < curr:
        levels.pop()
        t.type = 'END'
        t.lexer.lexpos -= len(t.value);
    else:
        t.lexer.lexpos -= 1;
        return None
    return t

# Error handling rule
def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#
# Não modificar esta função. Ela é usada para os testes.
#
def get_tokens(stream):
    global levels
    # Give the lexer some input
    lexer.input(stream)
    levels = [0]
    # Tokenize
    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break      # No more input
        tokens.append(token)
    return tokens