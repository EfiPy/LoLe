#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def Kmem8 (Length = None, Allocate = False):

  from LoLe                   import LoLeOp, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp    import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
    from LoLe.Driver.LinuxMmapDrv import PaDrv
  else:
    raise SystemError ('IO function Unsupport in this ABI')

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Kmem8Para = {
    'Name':         'Kmem8',
    'Length':       Length,
    'Step':         0x01,
    'Width':        8,
    'OpClass':      MemOp,
    'Driver':       PaDrv,
    'Private':      Allocate,
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeOp (Kmem8Para)
  # del (Kmem8Para)
  return ret

def Kmem16 (Length = None, Allocate = False):

  from LoLe                   import LoLeOp, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp    import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
    from LoLe.Driver.LinuxMmapDrv import PaDrv
  else:
    raise SystemError ('IO function Unsupport in this ABI')

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Kmem16Para = {
    'Name':         'Kmem16',
    'Length':       Length,
    'Step':         0x02,
    'Width':        16,
    'OpClass':      MemOp,
    'Driver':       PaDrv,
    'Private':      Allocate,
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeOp (Kmem16Para)
  # del (Kmem16Para)
  return ret

def Kmem32 (Length = None, Allocate = False):

  from LoLe                   import LoLeOp, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp    import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
    from LoLe.Driver.LinuxMmapDrv import PaDrv
  else:
    raise SystemError ('IO function Unsupport in this ABI')

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Kmem32Para = {
    'Name':         'Kmem32',
    'Length':       Length,
    'Step':         0x04,
    'Width':        32,
    'OpClass':      MemOp,
    'Driver':       PaDrv,
    'Private':      Allocate,
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeOp (Kmem32Para)
  # del Kmem32Para
  return ret

def Kmem64 (Length = None, Allocate = False):

  from LoLe                   import LoLeOp, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe.Operator.MemOp    import MemOp

  if    LOLE_ABI_STR == "PY64_WIN64_X86_64":
    from LoLe.Driver.WindowsKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY64_LINUX64_X86_64":
    from LoLe.Driver.LinuxKmDrv import PaDrv
  elif  LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
    from LoLe.Driver.LinuxMmapDrv import PaDrv
  else:
    raise SystemError ('IO function Unsupport in this ABI')

  if Length == None or Length == 0:
    raise ValueError ('Length cannot be None or Zero')

  Kmem64Para = {
    'Name':         'Kmem64',
    'Length':       Length,
    'Step':         0x08,
    'Width':        64,
    'OpClass':      MemOp,
    'Driver':       PaDrv,
    'Private':      Allocate,
    'FieldDict':    None,
    'Ds':           None,
  }

  ret = LoLeOp (Kmem64Para)
  # del (Kmem64Para)
  return ret
