from cx_Freeze import setup, Executable

base = None    

executables = [Executable("<<name.py>>", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<<name>>",
    options = options,
    version = "0.1",
    description = 'python',
    executables = executables
)
