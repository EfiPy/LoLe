#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def KmemShell (Length = None, Allocate = False):

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  from LoLe                   import LoLeShell, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp    import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import PaDrv
  # elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64" or LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
    from LoLe.Driver.LinuxMmapDrv import PaDrv
  else:
    raise SystemError ('IO function Unsupport in this ABI')

  KmemProfile = {
    'Name':         'Uint',
    'Length':       Length,
    # 'Step':         0x01,
    # 'Width':        8,
    'Layout':       ((8, 0x01), (16, 0x02), (32, 0x04), (64, 0x08)),
    'OpClass':      MemOp,
    'Driver':       PaDrv,
    'Private':      Allocate,
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeShell (KmemProfile)
