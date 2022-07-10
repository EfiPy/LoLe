#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def File8 (FileName = None, Flags = None, Mode = None, Length = None):

  if FileName == None:
    raise ValueError ('FileName cannot be None')

  from LoLe import LoLeOp
  from LoLe.Driver.FileDrv  import FileDrv
  from LoLe.Operator.MemOp  import MemOp

  File8Para = {
    'Name':         'File8',
    'Length':       Length,
    'Step':         0x01,
    'Width':        8,
    'OpClass':      MemOp,
    'Driver':       FileDrv,
    'Private':      (FileName, Flags, Mode),
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (File8Para)

def File16 (FileName = None, Flags = None, Mode = None, Length = None):

  if FileName == None:
    raise ValueError ('FileName cannot be None')

  from LoLe import LoLeOp
  from LoLe.Driver.FileDrv  import FileDrv
  from LoLe.Operator.MemOp  import MemOp

  File16Para = {
    'Name':         'File16',
    'Length':       Length,
    'Step':         0x02,
    'Width':        16,
    'OpClass':      MemOp,
    'Driver':       FileDrv,
    'Private':      (FileName, Flags, Mode),
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (File16Para)

def File32 (FileName = None, Flags = None, Mode = None, Length = None):

  if FileName == None:
    raise ValueError ('FileName cannot be None')

  from LoLe import LoLeOp
  from LoLe.Driver.FileDrv  import FileDrv
  from LoLe.Operator.MemOp  import MemOp

  File32Para = {
    'Name':         'File32',
    'Length':       Length,
    'Step':         0x04,
    'Width':        32,
    'OpClass':      MemOp,
    'Driver':       FileDrv,
    'Private':      (FileName, Flags, Mode),
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (File32Para)

def File64 (FileName = None, Flags = None, Mode = None, Length = None):

  if FileName == None:
    raise ValueError ('FileName cannot be None')

  from LoLe import LoLeOp
  from LoLe.Driver.FileDrv  import FileDrv
  from LoLe.Operator.MemOp  import MemOp

  File64Para = {
    'Name':         'File64',
    'Length':       Length,
    'Step':         0x08,
    'Width':        64,
    'OpClass':      MemOp,
    'Driver':       FileDrv,
    'Private':      (FileName, Flags, Mode),
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (File64Para)
