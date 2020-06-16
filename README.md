#Introduction  
**LoLe** is a Python library which is a reading/writing memory general purpose library and makes Python read/write byte/bit easily.  

Due to memory exists in different devices, LoLe read memory layout file (it is called profile, here) for different memory interface. In profile, it also defines memory access bit width.   

Current support system  
LoLe is designed as cross ISA/ABI library.  
`Python 3.5 3.6 3.7 3.8 for Linux/X86_64`  
`Python 3.5 3.6 3.7 3.8 for Raspbian/ARM-EABI5`
**LoLe** Library can be downloaded [here](https://sourceforge.net/projects/lole/).

#Copyright  
Copyright 2020 by MaxWu (EfiPy.core@gmail.com). All rights reserved.

#Sample  
In X86 system, assume pysical adress 0xB0000000 is MMIO address of one of PCI device.  
Following Python sample code tries to read 16 bits value stored in physical address 0xB0000000 and print it to console in Linux/X86_64 platform.
ReadUint16.py  
    from LoLe.KmemShell import KmemShell
    Kmem = KmemShell (0x10000000000000000)

    print ('Kmem[0xB0000000]... %s' % Kmem.Uint16[0xB0000000])
#Run  
    $ cd <LOLEPATH>
    $ export LOLE=$PWD
    $ cd <SamplePath>
    $ sudo PYTHONPATH=$LOLE python3 introduce.py
    Kmem[0xB0000000]......... 0x8086
    $
#Detail  
    from LoLe.KmemShell import KmemShell
**KmemShell** is LoLe function to produce reading/writing physical space object.  

    Kmem = KmemShell (0x10000000000000000)  
**KmemShell** return memory object **Kmem** which can read/write memory from physical space 0 to 0x10000000000000000 - 1.

    Kmem.Uint16[0xB0000000]
Kmem read **16 bits** value from physical address **0xB0000000**. It is the same as the C statement as below.  

    *(uint16_t *)(0xB0000000);

#Note  
*This is Linux command to get PCI MMIO start address in Linux system if it is a PCI-E device.*  

    sudo hexdump -C /sys/firmware/acpi/tables/MCFG
#Download LoLe Library  
Library [Download](https://sourceforge.net/projects/lole/)
[Blog](https://lolepython.blogspot.com/)
