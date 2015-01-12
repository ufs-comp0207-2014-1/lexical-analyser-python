# ------------------------------------------------------------
# lextests.py
#
# Tests for the Lexical Analyser
# ------------------------------------------------------------
__author__ = 'Gabriel Araujo'

import unittest
import test.samples as samples
import tinypyc.tinypylex as lex

def token_list(data):
    raw_token_list = lex.get_tokens(data)
    return [(t.type, t.value) if t.type == 'ID' else (t.type, ) for t in raw_token_list]

class LexicalAnalyserTest(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(samples.tokens_01, token_list(samples.data_01))
        self.assertListEqual(samples.tokens_02, token_list(samples.data_02))

if __name__ == '__main__':
    unittest.main()