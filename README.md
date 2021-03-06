# LOLE  
Python3 array library.  
Each element in array supports bitwise operation.  
LoLe uses subscript operator (square brackets []) to read/write address space in CPU or registers in peripheral.  
Different access target uses difference LoLe driver.  
# EXAMPLE - Bitwise operation
```
from LoLe.Mem import Mem32              # import Mem driver
TestMem = Mem32 (0x20)                  # allocate memory with 0x20bytes width
TestWord = TestMem[0x04]                # Set TestWord as 4 bytes (32bits) buffer from offset 0x04
TestWord[3] = 1                         # Set the 3rd bit as 1, other bits remain the same.
print (TestWord, TestWord[3])           # print TestWord and its 3rd bit.
TestWord[3] = 0                         # Set the 3rd bit as 0, other bits remain the same.
print (TestWord[3], TestWord[3])        # print TestWord and its 3rd bit, again.
```
# EXAMPLE - Write string to file
```
import os
TestStr = b'abcdefghijklmnopqrstuvwxyz' # string will be wrote to file by LoLe.

from LoLe.File import File8             # import File driver
TestFile = File8("Test.bin", os.O_RDWR | os.O_CREAT, Length=len(TestStr))
TestFile[:] = TestStr                   # Write TestStr to TestFile
```
# EXAMPLE - Read peripheral device via I2C bus.  
(root privilege)
```
from LoLe.I2c import I2c8       # import I2C driver.
pDevice = I2c8 (0, 0x24)        # Create I2C object bus address 0, slave address 0x24.
print (pDevice[0x02])           # Fetch and print register address 0x02.
```
# EXAMPLE - Read current year from X86 CMOS.
(root privilege)
```
from LoLe.Io import Io8         # import IO driver.
Io8= Io8 ()                     # Create IO object.
Io8[0x70] = 0x09                # Copy address 0x09 to CMOS register.
print (Io8[0x71])               # Fetch and print current year from CMOS.
```

# Read current year from X86 CMOS.
(root privilege)
```
from LoLe.Cmos import CmosInit  # import CMOS driver.
Cmos = CmosInit()               # Create CMOS object.
print (Cmos[0x09])              # Fetch and print current year from CMOS.
```
# More Examples
[Sample](https://github.com/EfiPy/LoLe)
[Blog](https://lolepython.blogspot.com/)
# Status  
LoLe supports Linux (X86_64, ARMv7, AARCH64) now.  
# Resource  
[Library](https://sourceforge.net/projects/lole/)
#Copyright  
Copyright 2020 by MaxWu (EfiPy.core@gmail.com). All rights reserved.
