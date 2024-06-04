# Batur Dinçer
# 220201018


rtypearr=["add","sub","and","or","sll","srl","sllv","srlv"]
itypearr=["addi","andi","sw","lw"]
itypejumparr=["beq","bne","bgtz","blez"]
jtypearr=["j"]
allinstructions=["add","sub","and","or","sll","srl","sllv","srlv","addi","andi","sw","lw","beq","bne","bgtz","blez","j"]
labelline= {}
startingAddress="0x00400000"
finalarray=[]
 
def setbranchlines(lines):
    global labelline
    counter=0
    for line in lines:
        if len(line)!=0 and line!=".text":
            if line.split()[0] not in allinstructions:
                labelname=line.split()[0].replace(" ","")
                labelname=labelname.replace(":","")
                labelline[labelname]=counter
            counter+=1

def findinstype(line):
    temparr= line.split()
    m=0
    cond=True
    while cond:
        if m<len(temparr):
            if temparr[m] in rtypearr:
                return "rtype"
            elif temparr[m] in itypearr:
                return "itype"
            elif temparr[m] in itypejumparr:
                return "itypejump"
            elif temparr[m] in jtypearr:
                return "jtype"
            else:
                m+=1
        else:
            break

def rType (line):
    machinecode=""
    funccode=""
    samtfo="00000"
    add="100000"
    sub="100010"
    andr="100100"
    orr="100101"
    sll="000000"
    sllv="000100"
    srl="000010"
    srlv="000110"
    opcode="000000" 

    temparr= line.split()
    m=0
    cond=True
    while cond:
        if temparr[m] in rtypearr:
            instruction=temparr[m]
            cond=False
        else:
            m+=1

    elements=[]
    curnum=""
    line=line.replace(" ", "")
    dollarcond=False
    for i in range(len(line)):
        if not line[i].isnumeric() and line[i]!="," and i!=len(line)-1 and line[i]!="$":
            continue
        elif line[i]=="$":
            dollarcond=True
            continue
        elif dollarcond and line[i].isnumeric():
            curnum+=line[i]
        elif not dollarcond and line[i].isnumeric():
            continue
        elif line[i]==",":
            curnumbin=bin(int(curnum))[2:].zfill(5)
            elements.append(curnumbin)
            curnum=""
        if i==len(line)-1:
            curnumbin=bin(int(curnum))[2:].zfill(5)
            elements.append(curnumbin)
            curnum=""
        
    if instruction !="sll" and instruction!="sllv" and instruction!="srl" and instruction!="srlv":
        if instruction=="add":
            funccode=add
        elif instruction=="sub":
            funccode=sub
        elif instruction=="and":
            funccode=andr
        elif instruction=="or":
            funccode=orr
        machinecode= opcode+ elements[1]+elements[2]+elements[0]+samtfo+funccode
    else:
        if instruction=="sll" or instruction=="srl":
            if instruction=="sll":
                funccode=sll
            else:
                funccode=srl
            machinecode= opcode+"00000"+elements[1]+elements[0]+elements[2]+funccode

        else:
            if instruction=="sllv":
                funccode=sllv
            elif instruction=="srlv":
                funccode==srlv
            machinecode=opcode+elements[2]+elements[1]+elements[0]+funccode
    return machinecode

def iType(line):
    machinecode=""
    temparr= line.split()
    m=0
    cond=True
    while cond:
        if temparr[m] in itypearr:
            instruction=temparr[m]
            cond=False
        else:
            m+=1

    elements=[]
    curnum=""
    dollarcond=False
    for i in range(len(line)):
        if not line[i].isnumeric() and line[i]!="," and i!=len(line)-1 and line[i]!="(" and line[i]!="$" and not dollarcond:
            continue
        elif line[i]=="$":
            dollarcond=True
            continue
        elif dollarcond and line[i]!="," and line[i]!=" ":
            curnum+=line[i]
        elif not dollarcond and line[i].isnumeric():
            continue
        elif line[i]=="," or line [i]=="(" or line[i]==")":
            if int(curnum)>=0:
                if len(elements)==0 or len(elements)==1:
                    curnumbin=bin(int(curnum))[2:].zfill(5)
                elif len(elements)==2:
                    curnumbin=bin(int(curnum))[2:].zfill(16)
                elements.append(curnumbin)
                curnum=""
            else:
                if(len(elements)==0 or len(elements)==1):
                    curnum=int(curnum[1:])
                    curnum=bin(curnum)[2:].zfill(5)
                    curnum=curnum.replace("0","2")
                    curnum=curnum.replace("1","0")
                    curnum=curnum.replace("2","1")
                    curnum=bin(int(curnum, 2)+1)[2:]

                elif len(elements)==2:
                    curnum=int(curnum[1:])
                    curnum=bin(curnum)[2:].zfill(16)
                    curnum=curnum.replace("0","2")
                    curnum=curnum.replace("1","0")
                    curnum=curnum.replace("2","1")
                    curnum=bin(int(curnum, 2)+1)[2:]
                elements.append(curnum)
                curnum=""

        if i==len(line)-1:
            if int(curnum)>=0:
                if (len(elements)==0 or len(elements)==1):
                    curnumbin=bin(int(curnum))[2:].zfill(5)
                elif len(elements)==2:
                    curnumbin=bin(int(curnum))[2:].zfill(16)
                elements.append(curnumbin)
                curnum=""
            else:
                if(len(elements)==0 or len(elements)==1):
                    curnum=int(curnum[1:])
                    curnum=bin(curnum)[2:].zfill(5)
                    curnum=curnum.replace("0","2")
                    curnum=curnum.replace("1","0")
                    curnum=curnum.replace("2","1")
                    curnum=bin(int(curnum, 2)+1)[2:]

                elif len(elements)==2:
                    curnum=int(curnum[1:])
                    curnum=bin(curnum)[2:].zfill(16)
                    curnum=curnum.replace("0","2")
                    curnum=curnum.replace("1","0")
                    curnum=curnum.replace("2","1")
                    curnum=curnum=bin(int(curnum, 2)+1)[2:]
                elements.append(curnum)
                curnum=""

    if instruction=="addi":
        machinecode="001000"+elements[1]+elements[0]+elements[2]
    elif instruction=="andi":
        machinecode="001100"+elements[1]+elements[0]+elements[2]
    elif instruction=="lw":
        machinecode="100011"+elements[2]+elements[0]+elements[1]
    elif instruction=="sw":
        machinecode="101011"+elements[2]+elements[0]+elements[1]
    return machinecode

def iTypeJump(line, curline):
    machinecode=""
    temparr= line.split()
    m=0
    cond=True
    while cond:
        if temparr[m] in itypejumparr:
            instruction=temparr[m]
            if instruction=="beq":
                opcode="000100"
            elif instruction=="bne":
                opcode="000101"
            elif instruction=="bgtz":
                opcode="000111"
            else:
                opcode="000110"
            cond=False
        else:
            m+=1

    elements=[]
    curnum=""
    dollarcond=False
    for i in range(len(line)):
        if not line[i].isnumeric() and line[i]!="," and i!=len(line)-1 and line[i]!="$" and not dollarcond:
            continue
        elif line[i]=="$":
            dollarcond=True
            continue
        elif dollarcond and line[i]!=",":
            if(line[i]==" "):
                continue
            curnum+=line[i]
        elif not dollarcond and line[i].isnumeric():
            continue
        elif line[i]==",":
            if instruction in ["beq","bne"]:
                curnumbin=bin(int(curnum))[2:].zfill(5)
                elements.append(curnumbin)
                curnum=""
            else:
                if len(elements)==0:
                    curnumbin=bin(int(curnum))[2:].zfill(5)
                    elements.append(curnumbin)
                    curnum=""
        if i==len(line)-1:
            targetline=labelline[curnum]
            targetline=targetline-(curline+1)
            if targetline<0:
                targetline=bin(int(str(targetline)[1:]))[2:].zfill(16)
                targetline=targetline.replace("0","2")
                targetline=targetline.replace("1","0")
                targetline=targetline.replace("2","1")
                targetline=bin(int(targetline, 2)+1)[2:]
            else:
                targetline=bin(targetline)[2:].zfill(16)
            elements.append(targetline)
            curnum=""

    if instruction=="beq":
        machinecode= opcode+elements[0]+elements[1]+elements[2]
    elif instruction=="bne":
            machinecode=opcode+elements[0]+elements[1]+elements[2]
    elif instruction=="bgtz":
        machinecode=opcode+elements[0]+"00000"+elements[1]
    else:
        machinecode=opcode+elements[0]+"00000"+elements[1]
    return machinecode

def jType(line):
    temparr=line.split()
    m=0
    cond=True
    while cond:
        if temparr[m] in jtypearr:
            opcode="000010"
            branchname=temparr[m+1]
            cond=False
        else:
            m+=1
    branchline=labelline[branchname]
    targetaddress=bin(int("0x00400000",16)+(branchline*4))[2:].zfill(32)[4:30]
    machinecode=opcode+targetaddress
    return machinecode

inputName=input("Enter file name: ")
with open (inputName, "r") as f:
    templines= f.readlines()
    lines=[]
    for line in templines:
        lines.append(line.strip())
    curline=0
    curaddress="0x00400000"
    setbranchlines(lines)
    for line in lines:
        if len(line)!=0 and line!=".text":
            if findinstype(line)=="rtype":
                text=curaddress+"                  "+"0x"+hex(int(rType(line),2))[2:].zfill(8)+"\n"
                finalarray.append(text)
            elif findinstype(line)=="itype":
                text= curaddress+"                  "+"0x"+hex(int(iType(line),2))[2:].zfill(8)+"\n"
                finalarray.append(text)
            elif findinstype(line)=="itypejump":
                text= curaddress+"                  "+"0x"+hex(int(iTypeJump(line,curline),2))[2:].zfill(8)+"\n"
                finalarray.append(text)
            elif findinstype(line)=="jtype":
                text= curaddress+"                  "+"0x"+hex(int(jType(line),2))[2:].zfill(8)+"\n"
                finalarray.append(text)
            
            curline+=1
            curaddress="0x"+hex(int(curaddress,16)+4)[2:].zfill(8)
    with open ("output.obj", "a") as file:
        file.writelines(finalarray)








