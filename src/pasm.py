# PASM stands for Plus Assembly and is an acronym for S++ Assembly
# Other names for PASM is SPP2ASM, S2ASM, SPP2NASM, S2NASM and etc.

import sys
import re
from warnings import warn

class PASM:
    @staticmethod
    def Transpile(codelist:list[str], outputname:str):
        with open(outputname + ".asm", "w") as f:
            for line in codelist:
                tabs = re.match(r'^\s*', line).group()
                if line.strip().startswith("if"):
                    cs = line.strip().replace(":", "").split(" ")
                    f.write(tabs + "cmp " + cs[1] + ", " + cs[3] + "\n")
                    if cs[2] == "==":
                        f.write(tabs + "je " + cs[4])
                    elif cs[2] == "!=":
                        f.write(tabs + "jne " + cs[4])
                    elif cs[2] == "<":
                        f.write(tabs + "jl " + cs[4])
                    elif cs[2] == ">":
                        f.write(tabs + "jg " + cs[4])
                    elif cs[2] == "u<":
                        f.write(tabs + "jb " + cs[4])
                    elif cs[2] == "u>":
                        f.write(tabs + "ja " + cs[4])
                    else:
                        f.write(tabs + "jmp " + cs[4])
                    f.write("\n")
                elif line.strip().find("=") != -1 and line.strip().find(":") == -1:
                    cs = line.strip().split(" ")
                    f.write(tabs + "mov " + cs[0] + ", " + cs[2] + "\n")
                else:
                    f.write(line)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        with open(sys.argv[1] + ".spp", "r") as f:
            try:
                PASM.Transpile(f.readlines(), sys.argv[2])
            except Exception:
                print("Transpiler has run into an error! Ensure the file exists or a typo happened!")
    else:
        print("""
Usage:
pasm [input filename (without extension)] [output filename (without extension)]
        """)