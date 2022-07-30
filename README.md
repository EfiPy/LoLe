# Introduction

Read/Write data by physical address

# Download

[LoLe-0.1.5.tgz](https://drive.google.com/file/d/1GmG3MZjCPvkD_viMJJRYj1IbNRsHCr00/view?usp=sharing)

# Installation (root privilege)

Install required package, first.  (As Ubuntu as example)  
```shell (root)
apt update
apt install build-essential
apt install linux-headers-$(uname -r)
apt install python3-pip
```
Install LoLe
```shell (root)
pip3 install LoLe-0.1.5.tgz
```

# Example

```
root:/sys/firmware/acpi/tables# hexdump -C MCFG
00000000  4d 43 46 47 3c 00 00 00  01 8c 42 4f 43 48 53 20  |MCFG<.....BOCHS |
00000010  42 58 50 43 20 20 20 20  01 00 00 00 42 58 50 43  |BXPC    ....BXPC|
00000020  01 00 00 00 00 00 00 00  00 00 00 00 00 00 00 b0  |................|
00000030  00 00 00 00 00 00 00 ff  00 00 00 00              |............|
0000003c
root:/sys/firmware/acpi/tables# python3
Python 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from LoLe.Kmem import Kmem8, Kmem16, Kmem32, Kmem64
-----------------------------------
LoLe version: 00.01.005
Author MaxWu (EfiPy.Core@gmail.com)
===================================
>>> Kmem = Kmem32 (0x10000000000000000)
>>> Kmem[0xB0000000]
Kmem32[0xb0000000:0xb0000003].bit[0:31]: 0x29C08086
>>> Kmem[0xB0000000][0:15]
Kmem32[0xb0000000:0xb0000003].bit[0:15]: 0x8086
>>>
```

# Blog
https://lolepython.blogspot.com/
