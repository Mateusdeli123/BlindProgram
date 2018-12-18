import re
import json
import requests
import time
import datetime

req_cotacao = requests.get('https://api.hgbrasil.com/finance')
cotacao = json.loads(req_cotacao.text)

while True:
    req = requests.get('https://api.hgbrasil.com/finance')
    cotacao = json.loads(req.text)
    print('')
    print('### Cotação ###')
    print('Dólar:',cotacao['results']['currencies']['USD']['buy'])
    print('Bitcoin:',cotacao['results']['currencies']['BTC']['buy'])
    print('Euro:',cotacao['results']['currencies']['EUR']['buy'])
    print('Tempo da Verificação:')
    time.sleep(5)

