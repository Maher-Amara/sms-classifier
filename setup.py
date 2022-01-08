import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == 'win32'):
    base = "Win32GUI"

setup(
    name="MonProgramme",
    version='0.1',
    description="none",
    executables=[Executable("interface.py", base=base, icon="icone.ico"), Executable("classifier.py"),
                 Executable("optimisation.py")],
    options={"build_exe": {"packages": ["tkinter"],
                           "include_files": ["ham_d1.txt", "sheet.txt", "spam_d1.txt", "icone.ico", "logo.png",
                                             "titre.png"]}}
)
