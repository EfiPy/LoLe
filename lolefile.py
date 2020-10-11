#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#
# 1. LoLe file driver
# 2. LoLe array setting
# 3. LoLe array iterator
# 4. LoLe bit setting
#

import os
from LoLe.File import File8, File16, File32, File64

#
# Test string b'abcdefghijklmnopqrstuvwxyz'.
#
TestName="lolefile.bin"
TestStr = b'abcdefghijklmnopqrstuvwxyz'

print ('Convert String in file to upper case')

#
# Create file and fill string b'abcdefghijklmnopqrstuvwxyz' in it.
#
testFile = File8(TestName, os.O_RDWR | os.O_CREAT, Length=len(TestStr))

testFile[:] = TestStr

#
# Dump file content
#
with open (TestName) as testFile2:
  print ('Test String.... ', testFile2.readline())

##############################################################################
#
# Convert to upper case by LoLe.
# lower case: The 5th bit is 1.
# upper case: The 5th bit is 0.
#
##############################################################################
print ()
print ('*** Convert string to upper case start ***')
for c in testFile:
  c[5] = 0
print ('*** Convert string to upper case stop ***')
print ()

#
# Dump file content, again.
# All characters are converted to upper case.
#
with open (TestName) as testFile2:
  print ('Convert result.... ', testFile2.readline())

