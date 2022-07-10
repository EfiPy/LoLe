#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#

def I2c8 (Bus, DevAddr):

  from LoLe                   import LoLeShell, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe import LoLeOp
  from LoLe.Operator.MemOp    import MemOp

  if  LOLE_ABI_STR == "PY64_LINUX64_X86_64" or LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
    from LoLe.Driver.LinuxI2cDrv import I2cDrv
  else:
    raise SystemError ('LoLe I2C function Unsupport in this ABI')

  I2c8Para = {
    'Name':         'I2c8',
    'Length':       0x100,
    'Step':         0x01,
    'Width':        8,
    'OpClass':      MemOp,
    'Driver':       I2cDrv,
    'Private':      (Bus, DevAddr),
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (I2c8Para)

def I2c16 (Bus, DevAddr):

  from LoLe                   import LoLeShell, LOLE_ABI_STR, LOLE_ABI_TAG
  from LoLe import LoLeOp
  from LoLe.Operator.MemOp    import MemOp

  if  LOLE_ABI_STR == "PY64_LINUX64_X86_64" or LOLE_ABI_STR == "PY32_LINUX_ARM_EABI":
    from LoLe.Driver.LinuxI2cDrv import I2cDrv
  else:
    raise SystemError ('LoLe I2C function Unsupport in this ABI')

  I2c16Para = {
    'Name':         'I2c16',
    'Length':       0x100,
    'Step':         0x01,
    'Width':        16,
    'OpClass':      MemOp,
    'Driver':       I2cDrv,
    'Private':      (Bus, DevAddr),
    'FieldDict':    None,
    'Ds':           None,
  }

  return LoLeOp (I2c16Para)

