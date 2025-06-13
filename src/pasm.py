# PASM stands for Plus Assembly and is an acronym for S++ Assembly
# Other names for PASM is SPP2ASM, S2ASM, SPP2NASM, S2NASM and etc.
# This transpiler is made by Duper NO! The main developer from the S++ community.
# It transpiles S++ code into NASM assembly code... Obviously.

import sys
import re
from warnings import warn

class PASM:
    @staticmethod
    def Transpile(codelist:list[str], outputname:str):
        with open(outputname + ".asm", "w") as f:
            for line in codelist:
                tabs = re.match(r'^\s*', line).group()
                if line.strip().lower().startswith("if"):
                    cs = line.strip().lower().replace(":", "").split(" ")
                    f.write(tabs + "cmp " + cs[1] + ", " + cs[3] + "\n")
                    if cs[2] == "==":
                        f.write(tabs + "je " + cs[4].split(",")[0])
                    elif cs[2] == "!=":
                        f.write(tabs + "jne " + cs[4].split(",")[0])
                    elif cs[2] == "<":
                        f.write(tabs + "jl " + cs[4].split(",")[0])
                    elif cs[2] == ">":
                        f.write(tabs + "jg " + cs[4].split(",")[0])
                    elif cs[2] == "u<":
                        f.write(tabs + "jb " + cs[4].split(",")[0])
                    elif cs[2] == "u>":
                        f.write(tabs + "ja " + cs[4].split(",")[0])
                    else:
                        f.write(tabs + "jmp " + cs[4].split(",")[0])
                    f.write("\n")
                    if cs[4].find(",") != -1 or len(cs) > 5:
                        if len(cs) > 5:
                            if cs[5].startswith(","):
                                f.write(tabs + "jmp " + cs[5].strip() + "\n")
                        else:
                            f.write(tabs + "jmp " + cs[4].split(",")[1].strip() + "\n")
                elif line.strip().lower().find("=") != -1 and line.strip().lower().find(":") == -1:
                    cs = line.strip().lower().split(" ")
                    f.write(tabs + "mov " + cs[0] + ", " + cs[2] + "\n")
                elif line.strip().lower() == "return" or "break":
                    f.write(tabs + "ret\n")
                elif line.strip().lower() == "bios":
                    cs = line.strip().lower().split(" ")
                    f.write(tabs + "int " + cs[1] + "\n")
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