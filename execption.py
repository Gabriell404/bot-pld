import requests as rq
import sys

class Exception:
    def __init__(self):
        self.url_api = 'http://10.54.56.51:8000/api/log'
        self.url_api_fim = 'http://10.54.56.51:8000/api/servico'

    def erro_generico(self, e):
        data = {
            "mensagem": f"Ops... Ocorreu o seguinte erro: {e}",
            "bot": "2"
        }

        resposta = rq.post(self.url_api, json=data)
        print(resposta)
        self.exit()

    def nenhum_registro_encontrado(self, i):
        data = {
            "mensagem": f"A ocorrência de número: {i}, não retorno nenhum registro.",
            "bot": "2"
        }
        resposta = rq.post(self.url_api, json=data)
        print(resposta)
        self.exit()

    def exit(self):
        sys.exit()