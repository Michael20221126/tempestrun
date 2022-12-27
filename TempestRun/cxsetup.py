#!/usr/bin/python
# coding=utf-8

import sys
from cx_Freeze import setup, Executable

sys.argv.append("build")
target_name = 'TempestRun.exe'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="TempestRun",
      author='Michael',
      version="1.0",
      executables=[Executable("main.py", targetName=target_name, icon="icon.ico", base=base)]
)

