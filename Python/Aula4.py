
# Com For
qtd_pessoas = int(input('Entre com a quantidade de pessoas '))
lista_pessoas = []

for pessoa in range(qtd_pessoas):
    nome = input('Digite nome da pessoa: ')
    lista_pessoas.append(nome)

print('Pessoas que foram convidadas para a festa: ', lista_pessoas)

print('---------------------------------------------------------------')

# Com While
qtd_pessoa = int(input('Entre com a quantidade de pessoas'))
lista_pessoas = []
count = 0;

while True:
    nome = input('Digite o nome da pessoa: ')
    lista_pessoas.append(nome)
    count += 1
    if (count == qtd_pessoa):
        break

print(lista_pessoas)