#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def MemShell (Length = None, Address = None):

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  from Mem._LoLe              import LoLeShell
  from LoLe.Driver.VaDrv      import VaDrv
  from LoLe.Operator.MemOp    import MemOp

  MemProfile = {
    'Name':         'Uint',
    'Length':       Length,
    # 'Step':         0x01,
    # 'Width':        8,
    'Layout':       ((8, 0x01), (16, 0x02), (32, 0x04), (64, 0x08)),
    'OpClass':      MemOp,
    'Driver':       VaDrv,
    'Private':      Address,
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeShell (MemProfile)
  return (ret)
