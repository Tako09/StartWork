import sys
from cx_Freeze import setup, Executable

base = None
copyDependentFiles = True
silent = True
base = None
packages = ['pyautogui']
includes = ['re', 'os']
excludes = []

# if sys.platform == "win32":
#     base = "Win32GUI"

setup(  name = "StartWork",
version = "1.0",
options = {"build_exe": {"includes":includes, "excludes":excludes, "packages": packages}},
executables = [Executable("work.py", base=base)])