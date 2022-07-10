#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def Mem8 (Length = None, Address = None):

  from LoLe import LoLeOp
  from LoLe.Driver.VaDrv import VaDrv
  from LoLe.Operator.MemOp import MemOp

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Mem8Para = {
    'Name':         'Mem8',
    'Length':       Length,
    'Step':         0x01,
    'Width':        8,
    'OpClass':      MemOp,
    'Driver':       VaDrv,
    'Private':      Address,
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (Mem8Para)

def Mem16 (Length = None, Address = None):

  from LoLe import LoLeOp
  from LoLe.Driver.VaDrv import VaDrv
  from LoLe.Operator.MemOp import MemOp

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Mem16Para = {
    'Name':         'Mem16',
    'Length':       Length,
    'Step':         0x02,
    'Width':        16,
    'OpClass':      MemOp,
    'Driver':       VaDrv,
    'Private':      Address,
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (Mem16Para)

def Mem32 (Length = None, Address = None):

  from LoLe import LoLeOp
  from LoLe.Driver.VaDrv import VaDrv
  from LoLe.Operator.MemOp import MemOp

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Mem32Para = {
    'Name':         'Mem32',
    'Length':       Length,
    'Step':         0x04,
    'Width':        32,
    'OpClass':      MemOp,
    'Driver':       VaDrv,
    'Private':      Address,
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeOp (Mem32Para)
  return ret

def Mem64 (Length = None, Address = None):

  from LoLe import LoLeOp
  from LoLe.Driver.VaDrv import VaDrv
  from LoLe.Operator.MemOp import MemOp

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Mem64Para = {
    'Name':         'Mem64',
    'Length':       Length,
    'Step':         0x08,
    'Width':        64,
    'OpClass':      MemOp,
    'Driver':       VaDrv,
    'Private':      Address,
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (Mem64Para)
