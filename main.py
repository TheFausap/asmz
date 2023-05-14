PRGMAX = 100
ORG = 300

prog = open('test.asm', 'r')
asm = open('test1.mem', 'w')
lblnf = False
pos = 0
orgpos = ORG
lines = prog.readlines()

count = 0
pc = 0
labels = [("", -1)]
vars = [("","",-1)]
consts = [("",-1)]
pmem = [""] * PRGMAX


def dbg():
    global vars
    global consts
    global labels
    # print(pmem)
    print("LABELS    USED: " + str(labels[1:]))
    print("VARIABLES USED: " + str(vars[1:]))
    print("CONSTANTS USED: " + str(consts[1:]))


def isint(v):
    try:
        vv = int(v)
    except ValueError:
        return False
    return True


def asmw(v):
    asm.write(str(v) + "\n")


def lblfind(l):
    global labels
    global lblnf
    for ll in labels:
        if l == ll[0]:
            return int(ll[1])
    lblnf = True
    return -1


def lblput(l):
    global labels
    if lblfind(l[0]) == -1:
        labels.append(l)


def varfind(l):
    global vars
    for ll in vars:
        if l == ll[0]:
            return int(ll[2])
    return -1


def varput(l):
    global vars
    if varfind(l[0]) == -1:
        vars.append(l)


def constfind(l):
    global consts
    for ll in consts:
        if l == ll[0]:
            return int(ll[1])
    return -1


def constput(l):
    global consts
    if varfind(l[0]) == -1:
        consts.append(l)


def bss(l,v):
    global vars
    global orgpos
    if varfind(l) == -1:
        varput((l,int(v),orgpos))
        orgpos = orgpos + int(v)
    asmw(2)
    asmw(v)
    asmw(1)
    asmw(4)


def cset(l,v):
    global consts
    if constfind(l) == -1:
        constput((l,int(v)))


def asmw1(v, p):
    vv = v[0]
    if vv == "ldir0":
        asmw(1)
    elif vv == "ldir1":
        asmw(49)
    elif vv == "sto":
        asmw(4)
    elif vv == "cla":
        asmw(20)
    elif vv == "adi":
        asmw(7)
    elif vv == "decr0":
        asmw(6)
    elif vv == "incr0":
        asmw(5)
    elif vv == "addm":
        asmw(8)
    elif vv == "sbi":
        asmw(9)
    elif vv == "subm":
        asmw(10)
    elif vv == "mui":
        asmw(11)
    elif vv == "mulm":
        asmw(12)
    elif vv == "idivi":
        asmw(13)
    elif vv == "idivm":
        asmw(14)
    elif vv == "outp":
        asmw(224)
    elif vv == "stpr":
        asmw(225)
    elif vv == "str6pr":
        asmw(226)
    elif vv == "str7pr":
        asmw(227)
    elif vv == "cpyr0":
        asmw(240)
    elif vv == "cpyr1":
        asmw(241)
    elif vv == "cpyr2":
        asmw(242)
    elif vv == "lor0":
        asmw(243)
    elif vv == "lor1":
        asmw(244)
    elif vv == "lor2":
        asmw(245)
    elif vv == "incr1":
        asmw(246)
    elif vv == "incr2":
        asmw(247)
    elif vv == "decr1":
        asmw(248)
    elif vv == "decr2":
        asmw(249)
    elif vv == "ldir2":
        asmw(250)
    elif vv == "ldir3":
        asmw(251)
    elif vv == "lor3":
        asmw(252)
    elif vv == "lor6":
        asmw(253)
    elif vv == "lor7":
        asmw(254)
    elif vv == "hlt":
        asmw(255)
    else:
        # label found
        lblput((v[0], p))
        vv = v[1]
        if vv == "ldir0":
            asmw(1)
        elif vv == "ldir1":
            asmw(49)
        elif vv == "sto":
            asmw(4)
        elif vv == "cla":
            asmw(20)
        elif vv == "adi":
            asmw(7)
        elif vv == "decr0":
            asmw(6)
        elif vv == "incr0":
            asmw(5)
        elif vv == "addm":
            asmw(8)
        elif vv == "sbi":
            asmw(9)
        elif vv == "subm":
            asmw(10)
        elif vv == "mui":
            asmw(11)
        elif vv == "mulm":
            asmw(12)
        elif vv == "idivi":
            asmw(13)
        elif vv == "idivm":
            asmw(14)
        elif vv == "outp":
            asmw(224)
        elif vv == "stpr":
            asmw(225)
        elif vv == "str6pr":
            asmw(226)
        elif vv == "str7pr":
            asmw(227)
        elif vv == "cpyr0":
            asmw(240)
        elif vv == "cpyr1":
            asmw(241)
        elif vv == "cpyr2":
            asmw(242)
        elif vv == "lor0":
            asmw(243)
        elif vv == "lor1":
            asmw(244)
        elif vv == "lor2":
            asmw(245)
        elif vv == "incr1":
            asmw(246)
        elif vv == "incr2":
            asmw(247)
        elif vv == "decr1":
            asmw(248)
        elif vv == "decr2":
            asmw(249)
        elif vv == "ldir2":
            asmw(250)
        elif vv == "ldir3":
            asmw(251)
        elif vv == "lor3":
            asmw(252)
        elif vv == "lor6":
            asmw(253)
        elif vv == "lor7":
            asmw(254)
        elif vv == "hlt":
            asmw(255)
        elif vv == ".bss":
            bss(v[0],v[2])
        elif vv == ".set":
            cset(v[0],v[2])
        else:
            print("1ukn")


def asmw2(v, p):
    global labels
    global lblnf
    global pos
    if v[0] == "loa":
        # no label
        asmw(2)
        if isint(v[1]):
            asmw(v[1])
        else:
            vf = varfind(v[1])
            cf = constfind(v[1])
            if (vf == -1) and (cf == -1):
                print("lblnfnd")
            elif vf != -1 and cf == -1:
                asmw(vf)
            elif vf == -1 and cf != -1:
                asmw(cf)
        pos = pos + 1
    elif v[0] == "jmp":
        asmw(48)
        if isinstance(v[1], int):
            asmw(v[1])
        else:
            lf = lblfind(v[1])
            if lf == -1:
                print("lblnfnd")
            else:
                asmw(lf)
        pos = pos + 1
    elif v[0] == "jzr":
        asmw(50)
        if isinstance(v[1], int):
            asmw(v[1])
        else:
            lf = lblfind(v[1])
            if lf == -1:
                print("lblnfnd")
            else:
                asmw(lf)
        pos = pos + 1
    elif v[0] == "jgt":
        asmw(54)
        if isinstance(v[1], int):
            asmw(v[1])
        else:
            lf = lblfind(v[1])
            if lf == -1:
                print("lblnfnd")
            else:
                asmw(lf)
        pos = pos + 1
    else:
        # label yes!
        lblput((v[0], p))
        if v[1] == "loa":
            asmw(2)
            if isinstance(v[2], int):
                asmw(v[2])
            else:
                vf = varfind(v[1])
                cf = constfind(v[1])
                if (vf == -1) and (cf == -1):
                    print("lblnfnd")
                elif vf != -1 and cf == -1:
                    asmw(vf)
                elif vf == -1 and cf != -1:
                    asmw(cf)
            pos = pos + 1
        elif v[1] == "jmp":
            asmw(48)
            if isinstance(v[2], int):
                asmw(v[2])
            else:
                lf = lblfind(v[2])
                if lf == -1:
                    print("lblnfnd")
                else:
                    asmw(lf)
            pos = pos + 1
        elif v[1] == "jzr":
            asmw(50)
            if isinstance(v[2], int):
                asmw(v[2])
            else:
                lf = lblfind(v[2])
                if lf == -1:
                    print("lblnfnd")
                else:
                    asmw(lf)
            pos = pos + 1
        elif v[1] == "jgt":
            asmw(54)
            if isinstance(v[2], int):
                asmw(v[2])
            else:
                lf = lblfind(v[2])
                if lf == -1:
                    print("lblnfnd")
                else:
                    asmw(lf)
            pos = pos + 1
        elif v[1] == ".bss" or v[1] == ".set":
            asmw1(v,p)
        else:
            # not real 2 arg opcode
            asmw1([v[1]], p)


def asml(l, p):
    global pos
    ll = l.split()
    print(ll)
    if ll[0] == ";":
        pos = pos - 1
    elif len(ll) == 1:
        asmw1(ll, p)
    elif len(ll) == 2 or len(ll) == 3:
        asmw2(ll, p)
    else:
        print("0ukn")


for lin in lines:
    pmem[count] = lin.strip()
    count = count + 1

for x in range(count):
    asml(pmem[pc], pc + pos)
    pc = pc + 1

if lblnf:
    print("Second pass...")
    asm.seek(0, 0)
    pc = 0
    for x in range(count):
        asml(pmem[pc], pc)
        pc = pc + 1

dbg()

prog.close()
asm.close()
