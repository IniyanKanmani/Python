
# Project available in https://repl.it/@lastlost/boilerplate-arithmetic-formatter#arithmetic_arranger.py

def signcon(x) :
    if x[1] == '+' :
        val = int(x[0]) + int(x[2])
    elif x[1] == '-' :
        val = int(x[0]) - int(x[2])
    else :
        val = "not+-"
    return str(val)

def arithmetic_arranger(problems, true = False):
    fstline = list()
    sndline = list()
    hyphen = list()
    sumorsub = list()
    printstring = ""
    if len(problems) > 5 :
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    for operation in problems :
        operation = operation.split()
        if not(operation[0].isdigit() and operation[2].isdigit()) :
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
        if len(operation[0]) > 4 or len(operation[2]) > 4 :
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
        if(signcon(operation) == "not+-") :
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        len0 = len(operation[0])
        len2 = len(operation[2])
        val = signcon(operation)
        if len0 == 1 :
            if len2 == 1 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(3)
                if len(val) == 1 :
                    sumorsub.append("  " + val)
                elif len(val) == 2 :
                    sumorsub.append(" " + val)
            elif len2 == 2 :
                fstline.append("   " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(4)
                if len(val) == 2 :
                    sumorsub.append("  " + val)
                elif len(val) == 3 :
                    sumorsub.append(" " + val)
            elif len2 == 3 :
                fstline.append("    " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(5)
                if len(val) == 3 :
                    sumorsub.append("  " + val)
                elif len(val) == 4 :
                    sumorsub.append(" " + val)
            elif len2 == 4 :
                fstline.append("     " + str(operation[0])[0])
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(6)
                if len(val) == 4 :
                    sumorsub.append("  " + val)
                elif len(val) == 5 :
                    sumorsub.append(" " + val)
        elif len0 == 2 :
            if len2 == 1 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + "  " + str(operation[2]))
                hyphen.append(4)
                if len(val) == 1 :
                    sumorsub.append("   " + val)
                elif len(val) == 2 :
                    sumorsub.append("  " + val)
                elif len(val) == 3 :
                    sumorsub.append(" " + val)
            elif len2 == 2 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(4)
                if len(val) == 1 :
                    sumorsub.append("   " + val)
                elif len(val) == 2 :
                    sumorsub.append("  " + val)
                elif len(val) == 3 :
                    sumorsub.append(" " + val)
            elif len2 == 3 :
                fstline.append("   " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(5)
                if len(val) == 3 :
                    sumorsub.append("  " + val)
                elif len(val) == 4 :
                    sumorsub.append(" " + val)
            elif len2 == 4 :
                fstline.append("    " + str(operation[0])[0])
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(6)
                if len(val) == 4 :
                    sumorsub.append("  " + val)
                elif len(val) == 5 :
                    sumorsub.append(" " + val)
        elif len0 == 3 :
            if len2 == 1 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + "   " + str(operation[2]))
                hyphen.append(5)
                if len(val) == 2 :
                    sumorsub.append("   " + val)
                elif len(val) == 3 :
                    sumorsub.append("  " + val)
                elif len(val) == 4 :
                    sumorsub.append(" " + val)
            elif len2 == 2 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + "  " + str(operation[2]))
                hyphen.append(5)
                if len(val) == 1 :
                    sumorsub.append("    " + val)
                elif len(val) == 2 :
                    sumorsub.append("   " + val)
                elif len(val) == 3 :
                    sumorsub.append("  " + val)
                elif len(val) == 4 :
                    sumorsub.append(" " + val)
            elif len2 == 3 :
                fstline.append(" " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(5)
                if len(val) == 1 :
                    sumorsub.append("    " + val)
                elif len(val) == 2 :
                    sumorsub.append("   " + val)
                elif len(val) == 3 :
                    sumorsub.append("  " + val)
                elif len(val) == 4 :
                    sumorsub.append(" " + val)
            elif len2 == 4 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(6)
                if len(val) == 1 :
                    sumorsub.append("     " + val)
                elif len(val) == 2 :
                    sumorsub.append("    " + val)
                elif len(val) == 3 :
                    sumorsub.append("   " + val)
                elif len(val) == 4 :
                    sumorsub.append("  " + val)
                elif len(val) == 5 :
                    sumorsub.append(" " + val)
        elif len0 == 4 :
            if len2 == 1 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + "    " + str(operation[2]))
                hyphen.append(6)
                if len(val) == 3 :
                    sumorsub.append("   " + val)
                elif len(val) == 4 :
                    sumorsub.append("  " + val)
                elif len(val) == 5 :
                    sumorsub.append(" " + val)
            elif len2 == 2 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + "   " + str(operation[2]))
                hyphen.append(6)
                if len(val) == 3 :
                    sumorsub.append("   " + val)
                elif len(val) == 4 :
                    sumorsub.append("  " + val)
                elif len(val) == 5 :
                    sumorsub.append(" " + val)
            elif len2 == 3 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + "  " + str(operation[2]))
                hyphen.append(6)
                if len(val) == 1 :
                    sumorsub.append("     " + val)
                elif len(val) == 2 :
                    sumorsub.append("    " + val)
                elif len(val) == 3 :
                    sumorsub.append("   " + val)
                elif len(val) == 4 :
                    sumorsub.append("  " + val)
                elif len(val) == 5 :
                    sumorsub.append(" " + val)
            elif len2 == 4 :
                fstline.append("  " + str(operation[0]))
                sndline.append(str(operation[1]) + " " + str(operation[2]))
                hyphen.append(6)
                if len(val) == 1 :
                    sumorsub.append("     " + val)
                elif len(val) == 2 :
                    sumorsub.append("    " + val)
                elif len(val) == 3 :
                    sumorsub.append("   " + val)
                elif len(val) == 4 :
                    sumorsub.append("  " + val)
                elif len(val) == 5 :
                    sumorsub.append(" " + val)
    for fi in fstline :
        printstring = printstring + fi + "    "
    printstring = printstring.rstrip() + "\n"
    for si in sndline :
        printstring = printstring + si + "    "
    printstring = printstring.rstrip() + "\n"
    for hi in hyphen :
        if hi == 3 :
            printstring = printstring + "---    "
        elif hi == 4 :
            printstring = printstring + "----    "
        elif hi == 5 :
            printstring = printstring + "-----    "
        elif hi == 6 :
            printstring = printstring + "------    "
    arranged_problems = printstring.rstrip()
    if true == True :
        printstring = printstring.rstrip() + "\n"
        for vi in sumorsub :
            printstring = printstring + vi + "    "
        arranged_problems = printstring.rstrip()
    return arranged_problems
