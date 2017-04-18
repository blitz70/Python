# data structure : searching and sorting, collections

import collections

text = "Python is a widely used high-level programming language for general-purpose programming, " \
       "created by Guido van Rossum and first released in 1991. An interpreted language, Python " \
       "has a design philosophy which emphasizes code readability (notably using whitespace " \
       "indentation to delimit code blocks rather than curly braces or keywords), and a syntax " \
       "which allows programmers to express concepts in fewer lines of code than possible in " \
       "languages such as C++ or Java.[22][23] The language provides constructs intended to enable " \
       "writing clear programs on both a small and large scale.[24] Python features a dynamic type " \
       "system and automatic memory management and supports multiple programming paradigms, " \
       "including object-oriented, imperative, functional programming, and procedural styles. " \
       "It has a large and comprehensive standard library.[25] Python interpreters are available " \
       "for many operating systems, allowing Python code to run on a wide variety of systems. " \
       "CPython, the reference implementation of Python, is open source software[26] and has a " \
       "community-based development model, as do nearly all of its variant implementations. " \
       "CPython is managed by the non-profit Python Software Foundation."
words = text.split()
print(words)

# searching item frequency in list
counts = collections.Counter(words)
print(counts.most_common(3))
print(counts)
