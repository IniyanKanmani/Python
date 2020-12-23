
# Project available in https://repl.it/@lastlost/boilerplate-arithmetic-formatter#arithmetic_arranger.py

def value(oper1,operand,oper2):
    if len(oper1) >= len(oper2):
        if operand == '+':
            return (((str(int(oper1) + int(oper2))).rjust(len(oper1) + 2)).ljust(len(oper1) + 6))
        else:
            return (((str(int(oper1) - int(oper2))).rjust(len(oper1) + 2)).ljust(len(oper1) + 6))
    else:
        if operand == '+':
            return (((str(int(oper1) + int(oper2))).rjust(len(oper2) + 2)).ljust(len(oper2) + 6))
        else:
            return (((str(int(oper1) - int(oper2))).rjust(len(oper2) + 2)).ljust(len(oper2) + 6))

def fstarrange(oper1,oper2):
    if len(oper1) >= len(oper2):
        return ((oper1.rjust(len(oper1) + 2)).ljust(len(oper1) + 6))
    else:
        return (oper1.rjust(len(oper2) + 2).ljust(len(oper2) + 6))

def sndarrange(oper1,operand,oper2):
    if len(oper1) >= len(oper2):
        return ((operand + ' ' + oper2.rjust(len(oper1))).ljust(len(oper1) + 6))
    else:
        return ((operand + ' ' + oper2).ljust(len(oper2) + 6))

def hyparrange(oper1,operand,oper2):
    if len(oper1) >= len(oper2):
        return (len(oper1) + 2)
    else:
        return (len(oper2) + 2)

def arithmetic_arranger(problems, true = False):
    fst = list()
    snd = list()
    hyp = list()
    thd = list()
    fstline = ""
    sndline = ""
    hypline = ""
    thdline = ""
    if len(problems) > 5:
        arranged_Problems = "Error: Too many problems."
        return arranged_Problems
    for prob in problems:
        oper = prob.split()
        if not(oper[1] == '+' or oper[1] == '-'):
            arranged_Problems = "Error: Operator must be '+' or '-'."
            return arranged_Problems
        if not(oper[0].isdigit() and oper[2].isdigit()):
            arranged_Problems = "Error: Numbers must only contain digits."
            return arranged_Problems
        if len(oper[0]) > 4 or len(oper[2]) > 4:
            arranged_Problems = "Error: Numbers cannot be more than four digits."
            return arranged_Problems
        fst.append(fstarrange(oper[0],oper[2]))
        snd.append(sndarrange(oper[0],oper[1],oper[2]))
        hyp.append(hyparrange(oper[0],oper[1],oper[2]))
        if true == True:
            thd.append(value(oper[0],oper[1],oper[2]))
    for val in fst:
        fstline = fstline + val
    fstline = fstline.rstrip()
    for val in snd:
        sndline = sndline + val
    sndline = sndline.rstrip()
    for val in hyp:
        for l in range(val):
            hypline = hypline + '-'
        hypline = hypline + '    '
    hypline = hypline.rstrip()
    arranged_Problems = fstline + "\n" + sndline + "\n" + hypline
    if true == True:
        for val in thd:
            thdline = thdline + val
        thdline = thdline.rstrip()
        arranged_Problems = arranged_Problems + "\n" + thdline
    return arranged_Problems
