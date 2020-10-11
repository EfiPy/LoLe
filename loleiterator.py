#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#
from LoLe.Mem import Mem16, Mem32
TestMem1 = Mem32 (0x20)
TestMem2 = Mem16 (0x20)

#
# Get size of LoLe object.
# The size unit is in bytes.
#
# TestMem1 and TestMem2 have the same length value.
#
print ('TestMem1 Length', len(TestMem1))
print ('TestMem2 Length', len(TestMem2))

#
# Get each element of TestMem1.
# Each element is 32 bits (4 bytes).
#
# TestMem1 has 0x20/4 elements.
#
print ('Dump each element in TestMem1')
for i in TestMem1:
  print (i)

#
# Get each element of TestMem2.
# Each element is 16 bits (2 bytes).
#
# TestMem2 has 0x20/2 elements.
#
print ('Dump each element in TestMem2')
for i in TestMem2:
  print (i)
