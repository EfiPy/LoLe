#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def FileShell (FileName = None, Flags = None, Mode = None, Length = 0x100):

  if FileName == None:
    raise ValueError ('FileName cannot be None')

  from LoLe._LoLe             import LoLeShell
  from LoLe.Driver.FileDrv    import FileDrv
  from LoLe.Operator.MemOp    import MemOp

  FileProfile = {
    'Name':         'Uint',
    'Length':       Length,
    # 'Step':         0x01,
    # 'Width':        8,
    'Layout':       ((8, 0x01), (16, 0x02), (32, 0x04), (64, 0x08)),
    'OpClass':      MemOp,
    'Driver':       FileDrv,
    'Private':      (FileName, Flags, Mode),
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeShell (FileProfile)
  return (ret)
