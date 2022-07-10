#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

from LoLe import LoLeOp
from LoLe.Operator.CmosOp import CmosOp

def CmosInit ():

  _CmosPyPara = {
    'Name':       'Cmos',
    'Length':     0x100,
    'Step':       1,              # used by BitOp slice function
    'Width':      8,              # (Done) used by BitOp, driver
    'OpClass':    CmosOp,
    'FieldDict':  None,           # used by BitOp
    'Ds':         None,           # used by BitOp
  }

  return LoLeOp (_CmosPyPara)
