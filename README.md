# TinyPy Lexical Analyser (Python)

Start code for building a TINYPy Lexical Analyser in Python. Check out the project description [here](https://github.com/ufs-comp0207-2014-1/tinypy-compiler).

## Project Structure

The project is organized in three folders:

* **ply**: where the sources of *PLY* library is located.
* **test**: where the test suites are located. Here, all the TinyPy sample codes are stored, as well as their test methods.
* **tinypyc**: where all the core files of the lexical analyser is located. The [`tinypylex.py`](tinypyc/tinypylex.py) file is the actual lexical analyser, with the lexical definitons, as well as the token generator procedures.

## PLY library

PLY is an implementation of lex and yacc parsing tools for Python.
In a nutshell, PLY is nothing more than a straightforward lex/yacc implementation. Here is a list of its essential features:

* It's implemented entirely in Python.
* It uses LR-parsing which is reasonably efficient and well suited for larger grammars.
* PLY provides most of the standard lex/yacc features including support for empty productions, precedence rules, error recovery, and support for ambiguous grammars.
* PLY is straightforward to use and provides very extensive error checking.
* PLY doesn't try to do anything more or less than provide the basic lex/yacc functionality. In other words, it's not a large parsing framework or a component of some larger system.

For more information about PLY Python library please visit the [PLY homepage](http://www.dabeaz.com/ply/). 
