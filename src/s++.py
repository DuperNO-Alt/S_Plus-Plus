# S++ is an Open-Source PL that is like Assembly, but has additional instructions
# S++ is currently x86_16 NASM-only

# S++ Follows a compiling step of: Transpiler (PASM) then Compiling (NASM)
# PASM is an Official Transpiler from S++ to NASM Assembly Code

# S++ Transpilers Are mainly written in Python

# Made by Duper NO!

# This script is for simplicity's sake, feel free to use PASM directly too.

import sys
import pasm as pasm
import os

print("S++ Transpiler made by Duper NO!")

if len(sys.argv) == 5:
    with open(sys.argv[1] + ".spp", "r") as f:
        try:
            pasm.PASM.Transpile(f.readlines(), sys.argv[2])
            print("Transpilation Complete (" + sys.argv[2] + "." + sys.argv[3] + ")")
        except Exception as e:
            print("Transpiler has run into an error! Ensure the file exists or a typo happened!")
            print(str(e))
            sys.exit(1)
    if sys.argv[4]:
        errorcode = os.system("nasm -f " + sys.argv[4] + " " + sys.argv[2] + ".asm" + " -o " + sys.argv[2] + "." + sys.argv[3])

        if errorcode != 0:
            print("Please install NASM or ensure the file exists! NASM error is Above ^")
            sys.exit(1)
        else:
            print("NASM compiled successfully.")
            os.remove(sys.argv[2] + ".asm")
            print("Temporary ASM file Deleted")
else:
    print("""
Usage:
s++ [input filename (without extension)] [output filename (without extension)] [output extension without .] [-f specification for NASM]
If [-f specification for NASM] isn't specified, it doesn't execute NASM (also keeps asm file)""")
