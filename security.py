import requests as rq

class Credencial:
    def __init__(self):
        # REQUESTS API
        self.request = rq.get('http://10.54.56.51:8000/api/credenciais/2')
        self.resposta = self.request.json()
        # ACESSANDO OS DADOS
        self.intranetUser = self.resposta[0]['intraUser']
        self.intranetPass = self.resposta[0]['intraPass']
        self.emailUser = self.resposta[0]['outlookUser']
        self.emailPass = self.resposta[0]['outlookPass']