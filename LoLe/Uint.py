#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#
from LoLe.Driver.UintDrv import DefaultWidth

def Uint (Value=None, BitWidth = DefaultWidth):

  from LoLe import LoLeOp
  from LoLe.Driver.UintDrv import UintDrv, MaxWidth
  from LoLe.Operator.MemOp import MemOp

  if BitWidth == None:
    BitWidth = DefaultWidth
  elif BitWidth > MaxWidth:
    raise IndexError ("BitWidth can not lager than 0x%X" % MaxWidth)

  UintPara = {
    'Name':         'UINT',
    'Length':       1,
    'Step':         0x01,
    'Width':        BitWidth,
    'OpClass':      MemOp,
    'Driver':       UintDrv,
    'Private':      Value,
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeOp (UintPara)
  return ret[0]
