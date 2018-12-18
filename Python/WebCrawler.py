import requests
import re
import io

arq = None
lista = []
requisicao = requests.get('http://www.repglobomaq.com.br')
req = requisicao.text
ra = re.search(r'.@',req)
if ra:
    print(ra.start())
else:
    print('Nada encontrado!')
