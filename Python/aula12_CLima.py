import requests
import json
import time

x = 0
repeticao = int(input('Numero de repetições:'))
while True:
    lista = []
    text = open('sites.txt',mode='r')
    c = 0

    for item in text:
       lista.append(item)

    while c < len(lista):
        req_clima = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+lista[c]+'&APPID=a4bf66274b60d4cdca7525e6c6f5bc24')
        j = json.loads(req_clima.text)
        temp_atual = j['main']['temp'] - 273.15
        temp_max = j['main']['temp_max'] - 273.15
        temp_min = j['main']['temp_min'] - 273.15
        print('Cidade:',lista[c],'Temperatura Atual:', round(temp_atual, 1), '\nTemperatura Maxima:', round(temp_max,1),
                  '\nTemperatura Minima:', round(temp_min,1))
        c = c + 1
        time.sleep(2)
        print('')
    x = x + 1
    if x == repeticao:
        print('FINISH')
        break













