#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def Io8 (Length = 0x10000):

  from LoLe import LoLeOp, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import IoDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import IoDrv
  else:
    raise SystemError ('This ABI does not support IO.')

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  _Io8Para = {
    'Name':       'Io8',
    'Length':     0x10000,
    'Step':       0x01,           # used by BitOp slice function
    'Width':      8,              # (Done) used by BitOp, driver
    'OpClass':    MemOp,
    'Driver':     IoDrv,
    'FieldDict':  None,           # used by BitOp
    'Ds':         None,           # used by BitOp
  }

  return LoLeOp (_Io8Para)

def Io16 (Length = 0x10000):

  from LoLe import LoLeOp, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import IoDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import IoDrv
  else:
    raise SystemError ('This ABI does not support IO.')

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  _Io16Para = {
    'Name':       'Io16',
    'Length':     0x10000,
    'Step':       0x02,           # used by BitOp slice function
    'Width':      16,             # (Done) used by BitOp, driver
    'OpClass':    MemOp,
    'Driver':     IoDrv,
    'FieldDict':  None,            # used by BitOp
    'Ds':         None,            # used by BitOp
  }

  return LoLeOp (_Io16Para)

def Io32 (Length = 0x10000):

  from LoLe import LoLeOp, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import IoDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import IoDrv
  else:
    raise SystemError ('This ABI does not support IO.')

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  _Io32Para = {
    'Name':       'Io32',
    'Length':     0x10000,
    'Step':       0x04,             # used by BitOp slice function
    'Width':      32,               # (Done) used by BitOp, driver
    'OpClass':    MemOp,
    'Driver':     IoDrv,
    'FieldDict':  None,            # used by BitOp
    'Ds':         None,            # used by BitOp
  }

  return LoLeOp (_Io32Para)
