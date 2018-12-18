import random
from random import choice

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
num_caract = int(input("Número de caracteres: "))
Ler_Arquivo = input('Você deseja ver a senha?')
arquivo = open('key.txt', 'w')

def password():
    if (num_caract < 0):
     return "Erro: número negativo"
    elif (num_caract == 0):
     return "Erro: Tem que ter pelo menos 1 caracter."
    else:
     passwd = ""
     while len(passwd) != num_caract:
         passwd = passwd + random.choice(char)
         if len(passwd) >= num_caract:
            arquivo.write(passwd)
            arquivo.close()
            return "Password: %s" % passwd

password()
def ler():
    arquivo = open('key.txt','r')
    for linha in arquivo:
        print(linha)

    arquivo.close()
if Ler_Arquivo == 's':
    ler()





