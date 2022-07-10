############################################################
#
# Copyright (c) 2020, Maxwu. All rights reserved.
#
#   EfiPy.core@gmail.com
#
############################################################
# from distutils.core import setup
from setuptools import setup

import os, sys, subprocess, platform

#
# Get LoLe ABI
#
# Linux-um64-km64-X86_64
# Linux-um64-km64-AARCH64
# Linux-um32-km32-ARMV7L
# Windows-um32-km64-X86_64
# Windows-um64-km64-X86_64
#
def GetInstallAbi ():

  TARGET_ABI = ''

  SYSTEM = platform.system ()  # (Linux, CYGWIN_NT, WIndows)
  if 'CYGWIN_NT' in SYSTEM:
    SYSTEM = 'CYGWIN_NT'

  MACHINE = platform.machine ()
  if MACHINE in ('x86_64', 'i686', 'AMD64'):
    MACHINE = 'X86_64'
    KM = 'km64'
  elif MACHINE in ('armv7l', ):
    MACHINE = 'ARMV7L'
    KM = 'km32'
  elif MACHINE in ('aarch64', ):
    MACHINE = 'AARCH64'
    KM = 'km64'

  UM, EXE = platform.architecture ()
  if UM == '64bit':
    UM = 'um64'
  elif UM == '32bit':
    UM = 'um32'
  else:
    UM = 'unknown'

  return f'{SYSTEM}-{UM}-{KM}-{MACHINE}', {'SYSTEM': SYSTEM, 'UM': UM, 'KM': KM, 'MACHINE': MACHINE}

#
# Build Kernel mode module
#
run_cmd = ['make']
if len(sys.argv) < 2:
 run_cmd = ['make']
elif sys.argv[1] in ('build', 'install', 'bdist_wheel', 'bdist'):
 run_cmd = ['make']
elif sys.argv[1] in ('clean'):
  run_cmd = ['make', 'clean']

_pwd = os.getcwd ()
_env = os.environ.copy ()
_env['PWD'] = os.path.join(_pwd, 'LoLe/Driver/Linux')
_env['TARGET_ABI'], InstallAbi = GetInstallAbi ()

if InstallAbi['SYSTEM'] == 'Linux':
  subprocess.run (run_cmd, env = _env, cwd = _env['PWD'])
  subprocess.run (['ln', '-nfs', './Linux/LinuxEp.ko', '../LinuxEp.ko'], env = _env, cwd = _env['PWD'])


InstallDir = ['LoLe', os.path.join ('LoLe', 'Driver'), os.path.join ('LoLe', 'Operator')]
for d in InstallDir:
  files = os.listdir(d)

  for f in files:

    if _env['TARGET_ABI'] in f:

      fsrc = os.path.join (d, f)
      fdst = os.path.join (d, f).replace (f".{_env['TARGET_ABI']}", "")

      if (os.path.isfile (fdst)):
         os.remove (fdst)

      if InstallAbi['SYSTEM'] == 'Linux' and sys.argv[1] != 'clean':
        os.symlink (f, fdst)

setup(
    name              = 'LoLe',
    version           = '0.1.4',
    description       = "Python array/bits operator",
    long_description  = "Python array/bits operator",
    long_description_content_type = "text/markdown",
    author            = "MaxWu",
    url               = "https://github.com/EfiPy/LoLe",
    author_email      = "EfiPy.Core@gmail.com",
    license           = 'CLOSED',
    platforms         = ['Linux', 'Windows'],
    classifiers=[
        'License :: Other/Proprietary License',
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: System :: Hardware',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: System :: Operating System Kernels :: Linux',

    ],
    packages          = ['LoLe', 'LoLe.Driver', 'LoLe.Operator'],
    package_dir       = {'LoLe': 'LoLe', 'LoLe.Driver': 'LoLe/Driver', 'LoLe.Operator': 'LoLe/Operator'},
    package_data      = {'LoLe': ['_LoLe.so'], 'LoLe.Operator': ['MemOp.so', 'CmosOp.so'], 'LoLe.Driver': ['VaDrv.so', 'UintDrv.so', 'LinuxKmDrv.so', 'LinuxMmapDrv.so', 'LinuxI2cDrv.so', 'FileDrv.so', '*.ko']},
)
