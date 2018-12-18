import re
import requests

try:

    req = requests.get('https://www.asuissa.com.br/aliancas-de-ouro')
    lista_nome = []
    lista_preco = []

    find_nome = re.findall(r'Aliança de Ouro \w+ \w+ \w+ - \w+', req.text)
    find_preco = re.findall(r'\w+[$] \w+.\w+,\w+',req.text)

    def getPreco():
        for item in find_preco:
                lista_preco.append(item)

    def getNome():
        for item in find_nome:
            if not item in lista_nome:
                 lista_nome.append(item)


    getNome()
    getPreco()

    print(lista_nome, '-\n', lista_preco)

except Exception as e:
    print('Houve um erro', e)

