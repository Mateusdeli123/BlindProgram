

lista = {5,4,6,8,10,22,4,6,55}

def MaiorNumero(lista):
    return max(lista)

print('Maior numero é', MaiorNumero(lista))

def MenorNumero(lista):
    return min(lista)

print('Menor numero é', MenorNumero(lista))


# Other example
qtd = int(input('Quantidade de vezes que irá repetir:'))

lista = []

def num(qtde):
    c = 1
    while c <= qtde:
        numero = int(input('Entre com os numeros:'))
        lista.append(numero)
        c = c + 1

    return lista

print(num(qtd))

