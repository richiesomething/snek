import cx_Freeze
import os

executables = [cx_Freeze.Executable("snake.py")]

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'

cx_Freeze.setup(name = "Snek",

                options = {
                    "build_ext" :{
                        "packages" : ["pygame"],
                        "include_files" : ["./apple.png", "./snekhead.png"],
                        "descriptioin" : "Old School Snake Game",
                    }

                },

                description = " Old Snake Game",
                executables = executables

                )