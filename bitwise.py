#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#
#
# This code explains how the LoLe basic bitwise operation is.
#
# LoLe has two operations: Array operation and bit operation.
# These operations are done by subscript operator (square brackets []).
#

#
# import Mem operation which is used for memory buffer.
#
from LoLe.Mem import Mem32

#
# Mem32 (0x20)
# Create 0x20 bytes buffer.
# TestMem is an array, each element holds 32bit data.
# It uses malloc to arrange system memory.
#
TestMem = Mem32 (0x20)

#
# Using subscript operator to denote any data in TestMem.
# The value in subscript operator after TestMem can be any value from 0 to 0x1F.
#
# TestMem[0x04]
# TestWord means part of the 4th to 7th bytes (32 bits)  data in TestMem.
# Any TestWord operation effects the 4th to the 7th bytes in TestMem. other data in TestMem remain the same.
#
# TestMem[0x04] is the same as TestMem[0x04:0x07].
#
TestWord = TestMem[0x04]                # Set TestWord as 4 bytes (32bits) buffer from offset 0x04

#
# Subscript operator after TestWord means the bit operation (read or write) to the data.
# The value in subscript operator after TesWord can be any value from 0 to 0x1F.
#
# the TestWord[3] = 1 implementation concept is denote in this pseudo code.
# (1 << 3) | (TestWird & (~(1 << 3)))
#
# the TestWord[3] = 0 implementation concept is denote in this pseudo code.
# (0 << 3) | (TestWird & (~(1 << 3)))
#
TestWord[3] = 1                         # Set the 3rd bit as 1, other bits remain the same.

#
# the TestWord[3] implementation concept is denote in this pseudo code.
# (TestWord >> 3) & 0x01
#
print (TestWord, TestWord[3])           # print TestWord and its 3rd bit.

TestWord[3] = 0                         # Set the 3rd bit as 0, other bits remain the same.
print (TestWord[3], TestWord[3])        # print TestWord and its 3rd bit, again.

