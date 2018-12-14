import sys

arg = sys.argv # METODO É O ARQ[1], ARG[2] É O PARAMETRO 1, ARG[3] É O PARAMETRO 3 E ASSIM POR DIANTE...

def soma(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1-num2

if arg[1] == 'soma':
    res = round(soma(float(arg[2]),float(arg[3])),2)

elif arg[1]== 'sub':
    res = round(sub(float(arg[2]),float(arg[3])),2)

print(res)
