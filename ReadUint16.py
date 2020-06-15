# import LoLe KmemShell library
from LoLe.KmemShell import KmemShell

# uint16_t *Kmem16 = (uint16_t *)0;
Kmem = KmemShell (0x10000000000000000)
Kmem16 = Kmem.Uint16

#
# Kmem.Uint16[0xB0000000] and Kmem16[0xB0000000] equal
#
# *(uint16 *)(0xB0000000)
#
print ('Kmem[0xB0000000]......... %s' % Kmem.Uint16[0xB0000000])
print ('Kmem16[0xB0000000]....... %s' % Kmem16[0xB0000000])
