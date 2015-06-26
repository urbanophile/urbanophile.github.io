Exploring the CPython intepreter II
###################################
:date: 2015-06-26
:tags: python, links, programming
:category: python
:authors: Matt Gibson
:summary: Resources for exploring the CPython interpreter.


When you run your python program, the basic flow is
my_program.py => compiler => bytecode => interpreter => output

The compiler builds an abstract syntax tree and converts.
Playing around with the cloc tool (handy)
CPython is about
3204 files and 978509 lines of code

cloc Python-2.7.8.tgz
    4271 text files.
    4170 unique files.
    1048 files ignored.

http://cloc.sourceforge.net v 1.62  T=28.25 s (113.4 files/s, 46149.7 lines/s)
---------------------------------------------------------------------------------------
Language                             files          blank        comment           code
---------------------------------------------------------------------------------------
Python                                2120          88008         108274         425222
C                                      548          50134          36977         370150
C/C++ Header                           254           6517           9912          64490
Bourne Shell                            41           6220           6581          41014
MSBuild script                          75              0              3          38436
m4                                      19           1588            191          15219
Assembly                                47           3659           4474          13733
make                                    12            500            361           3044
HTML                                    14            393             11           2344
Windows Module Definition                9            173            187           2079
Objective C                              7             98             61            635
Expect                                   7            115            178            545
DOS Batch                               30             92            102            449
CSS                                      1             98             19            328
Javascript                               3             31             49            229
Windows Resource File                    4             45             56            207
C++                                      2             27             18            134
vim script                               1             36              7            106
XML                                      4             57              2             73
NAnt script                              2              1              0             30
IDL                                      1              0              0             24
Visual Basic                             2              1              1             12
YAML                                     1              2              0              6
---------------------------------------------------------------------------------------
SUM:                                  3204         157795         167464         978509
---------------------------------------------------------------------------------------

The CPython interpreter is mostly written in C (surprise, surprise), and is a quite a substantial project
byte code is a basically assembly for python virtual machine. Python
2.7.8 has 147 different opcodes (operation codes) which implement the functionality of python. I have never really looked to closely at the python source code before, but there is a proposal to move Python to github which give it much more scrutiny. https://www.python.org/dev/peps/pep-0481/

Most of the action happens in ceval.c which is the main evaluation loop, and features a 1500 line long switch statement to handle all the opocodes  and c

Include/opcode.h
Python/ceval.c

The byte code reference is included in the dis module see here for further details https://docs.python.org/2/library/dis.html
There is a stackmachine implemented with

::
    >>> import dis
    >>> def catalan(n):
    ...    if n == 0:
    ...        return 1
    ...    else:
    ...        return (4* n - 2 ) * catalan(n-1) /(n+1)

    >>> catalan.func_code.co_code
    >>> '|\x00\x00d\x01\x00k\x02\x00r\x10\x00d\x02\x00Sd\x03\x00|\x00\x00\x14d\x04\x00\x18t\x00\x00|\x00\x00d\x02\x00\x18\x83\x01\x00\x14|\x00\x00d\x02\x00\x17\x15Sd\x00\x00S'
    >>> [ord(opcode) for opcode in catalan.func_code.co_code]
    [124, 0, 0, 100, 1, 0, 107, 2, 0, 114, 16, 0, 100, 2, 0, 83, 100, 3, 0, 124, 0, 0, 20, 100, 4, 0, 24, 116, 0, 0, 124, 0, 0, 100, 2, 0, 24, 131, 1, 0, 20, 124, 0, 0, 100, 2, 0, 23, 21, 83, 100, 0, 0, 83]
    >>> dis.dis(catalan)
      2           0 LOAD_FAST                0 (n)
                  3 LOAD_CONST               1 (0)
                  6 COMPARE_OP               2 (==)
                  9 POP_JUMP_IF_FALSE       16

      3          12 LOAD_CONST               2 (1)
                 15 RETURN_VALUE

      5     >>   16 LOAD_CONST               3 (4)
                 19 LOAD_FAST                0 (n)
                 22 BINARY_MULTIPLY
                 23 LOAD_CONST               4 (2)
                 26 BINARY_SUBTRACT
                 27 LOAD_GLOBAL              0 (catalan)
                 30 LOAD_FAST                0 (n)
                 33 LOAD_CONST               2 (1)
                 36 BINARY_SUBTRACT
                 37 CALL_FUNCTION            1
                 40 BINARY_MULTIPLY
                 41 LOAD_FAST                0 (n)
                 44 LOAD_CONST               2 (1)
                 47 BINARY_ADD
                 48 BINARY_DIVIDE
                 49 RETURN_VALUE
                 50 LOAD_CONST               0 (None)
                 53 RETURN_VALUE

Voila opcode!  You can see some discussion of the PyPy architecture choice for PyPy a speedier python interpeter which uses a JIT here.
http://www.aosabook.org/en/pypy.html
