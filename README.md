In this project, you will create a simple assembler program for the MIPS assembly language by using Java/Python programming language. Your program receives the source code filename (for example mycode.asm), translates each instruction into the machine code(HEX or Binary), and stores them with their associated address in an output file with the same name as the input file but with .obj extension.

For Simplicity, only consider the following MIPS instructions:

ADD, SUB, AND, OR, SLL, SRL, SLLV, SRLV (R-type)

ADDI, ANDI, LW, SW (I-Type)

BEQ, BNE, BLEZ, BGTZ  (I-type)

J  (J-type)

The source code in the input file can contain several instructions with different types, The target address of BEG, BNE, and J instructions are determined by labels in the source code.

The start Address of the program is 0x00400000

For example, consider the following source code

![image](https://github.com/baturdincer/MIPS-ASSEMBLER/assets/111300889/d5f0a495-b010-4f06-b084-0d706d721cc0)
