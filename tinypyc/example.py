__author__ = 'Gabriel Araujo'

import tinypyc.tinypylex as tokenizer

# Test it out
data = '''




if x :
    a
    if b:
      pass
      c
else:
    if d :
        if t0:
            pass




'''

stream_tokens = tokenizer.get_tokens(data)
for t in stream_tokens:
    print(t)