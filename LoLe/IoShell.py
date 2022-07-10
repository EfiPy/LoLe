#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def IoShell (Length = 0x10000):

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  from LoLe                   import LoLeShell, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp    import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import IoDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import IoDrv
  else:
    raise SystemError ('This ABI does not support IO.')

  IoProfile = {
    'Name':         'Io',
    'Length':       Length,
    # 'Step':         0x01,
    # 'Width':        8,
    'Layout':       ((8, 0x01), (16, 0x02), (32, 0x04)),
    'OpClass':      MemOp,
    'Driver':       IoDrv,
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeShell (IoProfile)
