#
# Copyrig 2020 by MaxWu (EfiPy.core@gmail.com)
#
# LoLe kernel space memory access sample code
#
# Target platform: Raspberry Pi 4, Raspbian
#

import time

from LoLe.KmemShell import KmemShell
Mem = KmemShell (0x10000000000000000)

#
# uint32_t *Kmem32 = (uint32_t *)0;
#
Kmem32  = Mem.Uint32

###################################################################################
#
# According to Broadcom BCM2385 ARM Peripherals document
#
###################################################################################

###################################################################################
#
# Set GPIO4 as output mode.
#
###################################################################################
#
# GPFSEL0 (0xFE200000) bit 12-14, GPIO pin 4 function selection.
#                                 b001, output
#
# *((uint32_t *)0xFE200000) = (*((uint32_t *)0xFE200000) & ~(7 << 12)) | (1 << 12);
#
Kmem32[0xFE200000][12:14] = 1

###################################################################################
#
# Set GPIO4 as high level.
#
###################################################################################
#
# 0xFE20001C, GPIO Pin Output Set 0
# bit 4,      GPIO4
#
# *((uint32_t *)0xFE20001C) = 1 << 4;
#
Kmem32[0xFE20001C] = 1 << 4

###################################################################################
#
# Set GPIO9 as input mode.
#
###################################################################################
#
# GPFSEL0 (0xFE200000) bit 24-26, GPIO pin 8 function selection.
#                                 b000, input
#
# Set bit 27-29 of address 0xFE200034 value as 0
#
# *((uint32_t *)0xFE200000) = (*((uint32_t *)0xFE200000) & ~(7 << 27)) | (0 << 27);
#
Kmem32[0xFE200000][27:29] = 0 # GPIO9

###################################################################################
#
# Get GPIO9 value
#
###################################################################################
#
# 0xFE200034, GPIO Pin Level 0
# bit 9,      GPIO9
#
# Pick 9'th bit of address 0xFE200034.
#
# # define gpio9  (*((uint32_t *)0xFE200034) >> 9) & 0x00000001
#
gpio9 = Kmem32[0xFE200034][9]

while True:
  # (*((uint32_t *)0xFE200034) >> 9) & 0x00000001;
  print ("gpio9(2) ", Kmem32[0xFE200034][9])
  print ("gpio9(1) ", gpio9)
  time.sleep (1)
