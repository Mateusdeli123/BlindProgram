import requests

try:
    def PostInfo():
        login = {'username':'globomaq',
                 'password':'matheus4564'}

        cookies = {'Utima visita':'454654564'}

        hearder = {'USER-AGENT':'LocaoDoCrack'}

        requisicao = requests.post('https://putsreq.com/MJXvUZ08o0z9WFmDs04R',
                            data=login,
                            cookies=cookies,
                            headers=hearder)
        print(requisicao.text)

    def getInfo():
        return requests.get('https://putsreq.com/MJXvUZ08o0z9WFmDs04R')


    print(getInfo())
except Exception as e:
    print('Erro na requisição', e)