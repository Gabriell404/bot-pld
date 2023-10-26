import pyautogui as py
import security
import pyperclip
import re
import requests as rq
import cv2 as cv
import datetime
import string
import execption


class Metodos:
    def __init__(self):
        self.security = security.Credencial()
        self.erro = execption.Exception()

    # FUNÇÃO QUE REALIZA A ABERTURA DO BROWSER 
    def abrir_browser(self):
        self.img_browser_aberto = py.locateOnScreen('img/browserAberto.png', confidence=0.9)
        if (self.img_browser_aberto is None):
            py.hotkey('ctrl', 'esc')
            py.time.sleep(1.5)
            py.write('Brave')
            py.time.sleep(1.7)
            py.press('enter')
            print('abrir')
        else:
            print('Fechar')
            self.fechar_browser()

    # FUNÇÃO QUE É CHAMADA SE O BROWSER ESTIVER ABERTO NO INICIO DO PROCESSO 
    def fechar_browser(self):
        self.img_browser_aberto = py.locateOnScreen('img/browserAberto.png', confidence=0.9)
        self.posicao_brave = py.center(self.img_browser_aberto)
        py.moveTo(self.posicao_brave)
        py.click()
        py.time.sleep(1.5)
        py.hotkey('alt', 'f4')
        py.time.sleep(1.5)
        py.press('enter')
        py.time.sleep(1.8)
        self.abrir_browser()
        
    # FUNÇÃO QUE REALIZA A ABERTURA DO SISBR 
    def abri_sisbr(self):
        pass

    # FUNAÇÃO QUE VERIFICA SE O BROWSER CARREGO POR COMPLETO
    def analisa_carregamento_browser(self):
        py.time.sleep(2)
        while True:
            self.img_browser_carregado = py.locateOnScreen('img/inicialBrowser.png', confidence=0.7)
            if (self.img_browser_carregado is None):
                py.time.sleep(1)
                print('Ixa')
            else:
                break

    # FUNÇÃO QUE ACESSA A PÁGINA DO EMAIL E INTRANET 
    def acessar_sites(self):
        pyperclip.copy('https://outlook.office365.com/')
        py.hotkey('ctrl', 'v')
        py.press('enter')
        # self.login_email()
        py.hotkey('ctrl', 't')
        py.time.sleep(1.5)
        pyperclip.copy('https://intranet.sicoobaracoop.com.br/')
        py.hotkey('ctrl', 'v')
        py.press('enter')
        self.login_intranet()
        py.hotkey('ctrl', 'tab')

    # FUNÇÃO QUE EFETUA LOGIN NO E-MAIL
    def login_email(self):
        while True:
            self.img_inicial_email = py.locateOnScreen('img/inicialEmail.png', confidence=0.9)
            if (self.img_inicial_email is None):
                py.time.sleep(1)
            else:
                py.write(self.security.emailPass)
                py.press('enter')
                break

    # FUNÇÃO QUE EFETUA LOGIN NA INTRANET
    def login_intranet(self):
        while True:
            self.img_inicial_intranet = py.locateOnScreen('img/inicialIntra.png', confidence=0.7)
            if (self.img_inicial_intranet is None):
                py.time.sleep(1)
            else:
                py.press('tab')
                py.write(self.security.intranetUser)
                py.time.sleep(0.9)
                py.press('tab')
                py.write(self.security.intranetPass)
                py.time.sleep(0.8)
                py.press('enter')
                break

    # FUNÇÃO QUE ACESSA A PASTA PLD/FT 
    def acessar_pasta_pld(self):
        py.press('f5')
        py.time.sleep(2)
        while True:
            self.img_pasta = py.locateOnScreen('img/pastaPLD.png', confidence=0.9)
            if (self.img_pasta is None):
                py.time.sleep(1)
            else:
               self.posicao_pasta = py.center(self.img_pasta)
               py.moveTo(self.posicao_pasta)
               py.click()
               py.time.sleep(2)
               break

    # FUNÇÃO QUE ATUALIZA A PASTA 
    def att_pasta_pld(self):
        py.press('f5')
        py.time.sleep(1.5)
        
    # FUNÇÃO QUE ANALISA SE A APSTA ESTA CHEIA OU VAZIA
    def analisa_pasta_pld(self):
        self.pasta_cheia = ''
        py.time.sleep(1)
        self.img_pasta_vazia = py.locateOnScreen('img/pastaVazia.png')
        if (self.img_pasta_vazia is None):
            self.pasta_cheia = 'sim'
            print(self.pasta_cheia)
        else:
            self.pasta_cheia = 'nao'
            print(self.pasta_cheia)

    def moviment(self):
        py.moveTo(150, 500)
        py.time.sleep(2)
        py.hscroll(500)
        py.hscroll(-500)
        py.time.sleep(1.5)

    # FUNÇÃO QUE REALIZA MOVIMENTOS SE A PASTA ESTIVER VAZIA 
    def ocioso(self):
        self.moviment()
        self.alt_pagina()
        self.moviment()
        self.alt_pagina()
        self.acessar_sisbr()
        self.moviment()
        self.retorna_browser()
        self.att_pasta_pld()
        self.analisa_pasta_pld()
        self.acessar_email()

    # FUNÇÃO QUE ACESSA O EMAIL 
    def acessar_email(self):
        if (self.pasta_cheia == 'sim'):
            while True:
                self.img_email_fechado = py.locateOnScreen('img/novoEmail.png', confidence=0.9)
                if(self.img_email_fechado is None):
                    py.time.sleep(1)
                else:
                    self.posicao_novo_email = py.center(self.img_email_fechado)
                    py.moveTo(self.posicao_novo_email[0] + 25, self.posicao_novo_email[1])
                    py.click()
                    break
            py.time.sleep(0.9)
        else:
            self.ocioso()

    # FUNÇÃO QUE PEGA O TEXTO DO EMAIL 
    def get_texto_email(self):
        py.time.sleep(2)
        py.time.sleep(3.5)
        py.press('tab', presses=6)
        py.time.sleep(1)
        py.hotkey('ctrl', 'a')
        py.hotkey('ctrl', 'c')
        self.texto_email = pyperclip.paste()
        print(self.texto_email)
        py.time.sleep(0.3)
        py.click()
        py.time.sleep(1.1)
        py.press('e')
        py.time.sleep(2)

    # FUNÇÃO QUE EXTRAI O NUMERO DA OCORRENCIA 
    def get_numero_ocorrencia(self):
        self.numero_ocorrencia = re.search(r'ocorrência (\d+)', self.texto_email)
        print(self.numero_ocorrencia)

        if (self.numero_ocorrencia):
            print(self.numero_ocorrencia.group(1))
            py.time.sleep(1)
        else:
            self.erro.erro_generico('Não foi possivel encontrar o número da ocorrência no texto do email. A automação foi interrompida.')


    # ACESSANDO O SISBR
    def acessar_sisbr(self):
        self.img_icon_sisbr = py.locateOnScreen('img/iconSisbr.png', confidence=0.9)

        if(self.img_icon_sisbr is None):
            self.erro.erro_generico('O icone do Sisbr não foi encontrado. A automação foi interrompida.')
        else:
            self.posicao_icone_sisbr = py.center(self.img_icon_sisbr)
            py.moveTo(self.posicao_icone_sisbr)
            py.click()

    # FUNÇÃO QUE PESQUISA POR PLD/FT 
    def pesquisar_pld(self):
        while True:
            self.img_campo_pesquisa_sisbr = py.locateOnScreen('img/pesquisaSisbr.png', confidence=0.7)
            if (self.img_campo_pesquisa_sisbr is None):
                py.time.sleep(1)
            else:
                self.posicao_pesquisa = py.center(self.img_campo_pesquisa_sisbr)
                py.moveTo(self.posicao_pesquisa)
                py.click()
                py.write('pld/ft')
                py.press('enter')
                py.time.sleep(1.5)
                py.press('tab')
                py.press('enter')
                break

    # FUNÇÃO QUE ENTRA NO PAINEL DE ANALISE DE OCORRENCIA 
    def acessar_painel_analise_ocorrencia(self):
        while True:
            self.img_analise_ocorrencia = py.locateOnScreen('img/analiseOcorrenciaBusca.png', confidence=0.9)
            if (self.img_analise_ocorrencia is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1.5)
                py.press('tab', presses=3)
                py.press('enter')
                py.write('ANALISE DE OCORRENCIAS')
                py.time.sleep(1.2)
                py.press('enter')
                py.time.sleep(1)
                py.press('down', presses=2)
                break

    # FUNÇÃO QUE PREENCHE O CAMPO COM ID 
    def insert_campo_id(self):
        while True:
            self.img_campo_id = py.locateOnScreen('img/campoIdOcorrencia.png', confidence=0.8)
            if (self.img_campo_id is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1.5)
                py.press('tab', presses=4)
                pyperclip.copy(self.numero_ocorrencia.group(1))
                py.hotkey('ctrl', 'v')
                py.time.sleep(0.9)
                break

    # FUNÇÃO QUE CLICKA NO BT ANALISAR 
    def press_analissar(self):
        py.time.sleep(1.5)
        py.press('tab', presses=31)
        py.time.sleep(1.5)
        py.press('enter')
        py.time.sleep(0.9)

    # FUNÇÃO QUE PRESIONA O BOTÃO PESQUISAR 
    def press_pesquisar(self):
        py.press('tab', presses=27)
        py.time.sleep(0.9)
        py.press('enter')

    # FUNÇÃO QUE VAI PARA A TELA DE ANALISE DENTRO DA PARTE DE 'COSULTA GERENCIAL'
    def acessar_analises(self):
        while True:
            self.img_tela_consulta_gerencial = py.locateOnScreen('img/consultaGerencial.png', confidence=0.8)
            if (self.img_tela_consulta_gerencial is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1.2)
                py.press('tab', presses=1)
                py.time.sleep(1.2)
                py.press('right')
                py.time.sleep(1.2)
                py.press('enter')
                break

    # FUNÇÃO QUE ACESSA O PRIMEIRO REGISTROE EM ANALISES 
    def acessar_primeiro_registro_analises(self):
        while True:
            self.img_dentro_analises = py.locateOnScreen('img/dentroDeAnalises.png', confidence=0.8)
            if (self.img_dentro_analises is None):
                py.time.sleep(1)
            else:
                self.posicao_dentro_analises = py.center(self.img_dentro_analises)
                py.moveTo(self.posicao_dentro_analises)
                py.click()
                py.time.sleep(1)
                py.press('tab')
                py.time.sleep(1)
                py.press('enter')
                break

    # FUNÇÃO QUE PEGA O TEXTO BASE DO PLD 
    def get_texto_pld(self):
        while True:
            self.img_texto_pld_carregado = py.locateOnScreen('img/textoPldCarregado.png', confidence=0.9)
            if (self.img_texto_pld_carregado is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1)
                py.press('tab', presses=6)
                py.time.sleep(1)
                py.hotkey('ctrl', 'a')
                py.time.sleep(0.7)
                py.hotkey('ctrl', 'c')
                self.texto_pld = pyperclip.paste()
                py.press('esc')
                py.time.sleep(1.1)
                break


    # ANALISANDO TELA DE CARREGAMENTO OCORRENCIA 
    def analisa_tela_carregamento_ocorrencia(self):
        while True:
            self.img_tela_carregamento_ocorrencia = py.locateOnScreen('img/telaDeCarregamentoOcorrencias.png', confidence=0.8)
            if (self.img_tela_carregamento_ocorrencia is None):
                break
            else:
                py.time.sleep(1)

    # FUNÇÃO QUE ANALISA SE EXISTE REGISTRO PARA O NUMERO DE OCORRENCIA QUE FOI INFORMADO 
    def existe_ocorrencia(self):
        self.tem_ocorrencias = ''
        self.analisa_tela_carregamento_ocorrencia()
        self.img_nenhum_registro = py.locateOnScreen('img/nenhumRegistroEncontrado.png', confidence=0.8)
        if (self.img_nenhum_registro is None):
            self.tem_ocorrencias = 'sim'
            print('Existe ocorrencias')
        else:
            self.tem_ocorrencias = 'nao'
            print('Não possui')
            self.fechar_janelas()
            py.time.sleep(0.9)
            self.limpa_campo()
            self.erro.nenhum_registro_encontrado(self.numero_ocorrencia)

    # FUNÇÃO QUE FECHA JANELAS
    def fechar_janelas(self):
        py.time.sleep(1)
        py.hotkey('alt', 'f4')

    # FUNÇÃO QUE ANALISA SE A TELA É A INICIAL DO SISBR 
    def inicial_sisbr(self):
        py.time.sleep(1.9)
        self.inicial_sisbr = ''
        self.img_inicial_sisbr = py.locateOnScreen('img/inicialSisbr.png', confidence=0.8)
        if (self.img_inicial_sisbr is None):
            self.inicial_sisbr = 'nao'
        else:
            self.inicial_sisbr = 'sim'


    # FUNÇÃO QUE LIMPA O CAMPO DE BUSCA DO SISBR 
    def limpa_campo(self):
        py.time.sleep(1.7)
        self.inicial_sisbr()
        if (self.inicial_sisbr == 'sim'):
            self.img_del = py.locateOnScreen('img/limparTela.png', confidence=0.8)
            self.posicao_del = py.center(self.img_del)
            py.moveTo(self.posicao_del)
            py.click()
        else:
            self.erro.erro_generico('Algo de diferente ocorreu, não estamos na tela inicial do Sisbr. A automação foi interrompida.')
    
    # FUNÇÃO QUE RETORNA A DATA ATUAL + 3 DIAS PULANDO SABADO E DOMINGO
    def retorna_data(self):
        self.data_inicial = datetime.date.today()
        dias_uteis = datetime.timedelta(days=1)

        dias_contados = 0
        while dias_contados < 3:
            self.data_inicial += dias_uteis
            if self.data_inicial.weekday() >= 5:
                continue
            else:
                dias_contados += 1
        print(self.data_inicial)

    def tratamento_texto_pld(self):
        texto_que_se_econtra_em_cc = '- RESTRITO - As informações contidas no dossiê de PLD/FT'
        if (texto_que_se_econtra_em_cc in self.texto_pld):
            self.tratamento_texto_pld_cc()
            print("Texto é um CC")
        else:
            self.tratamento_texto_pld_poupanca()
            print("Texto é uma poupanca")


    # FUNÇÃO QUE FAZ A MONTAGEM DO TEXTO QUE VAI SER INSERIDO NA ABERTURA DO CHAMADO QUANDO A CONTA FOR POUPANÇA 
    def tratamento_texto_pld_poupanca(self):
        texto_word_etapa2 = '''QUESTIONÁRIO:


        Questão 01:
        Utilizando o princípio conheça seu cooperado, explique quem é o associado alertado, qual a sua área de atuação, fluxo de renda e forneça informações que nos ajude a entender a sua movimentação.

        Questão 02: 
        Explique os principais créditos e débitos ocorridos no mês em questão, bem como suas respectivas origens e destinos. 

        Questão 03:
        Qual a justificativa para a movimentação acima da capacidade declarada em cadastro?

        Questão 04:
        O gerente possui informações de algum fato adicional que agregue a sua resposta? Caso positivo, relatar o fato detalhadamente.


        -------------------------------------------------------------------------------------------------------------------- 
        IMPORTANTE: 
        - Para as respostas que tenham comprovação documental, os documentos devem ser anexados nesta ocorrência (aba anexo) para compor o dossiê digital.
        - Vale destacar, que as respostas não conclusivas prejudicam as diligências e podem ser marcadas na Plataforma PLD/FT como *"INSUFICIÊNCIA da aplicação do princípio conheça seu cooperado/cliente", que pode ser considerado elegível para comunicação ao BCB, conforme descrito na Política Institucional de Fatos Relevantes do Sicoob. 
        - Destacamos que a aplicação do princípio conheça seu cooperado/cliente é regulada pelo Comitê Basiléia e Circular Bacen nº 3.978/2020.
        - As informações prestadas pelo gerente responsável pela conta, subsidiam a recomendação de finalização da ocorrência com ou sem comunicação ao COAF, consideramos, que as informações inseridas na resposta do questionário, serão checadas, analisadas e verdadeiras.
   
        '''
        situacao_motivadora = self.texto_pld.find('SITUAÇÕES MOTIVADORAS DA OCORRÊNCIA:')

        if (situacao_motivadora != -1):
            trecho = self.texto_pld[situacao_motivadora:]

            self.texto_pld = self.texto_pld.replace(trecho, '')

            if ('Poupador:' in self.texto_pld):
                self.texto_pld = self.texto_pld.replace('Poupador:', trecho + '\n\nPoupador:')
            elif ('Poupadora:' in self.texto_pld):
                self.texto_pld = self.texto_pld.replace('Poupadora:', trecho + '\n\nPoupador:')

            self.texto_etapa_cinco = self.texto_pld + texto_word_etapa2

        print(f'Esse é o texto do poupador?: {self.texto_etapa_cinco}')



    # FUNÇÃO QUE FAZ A MONTAGEM DO TEXTO QUE VAI SER INSERIDO NA ABERTURA DO CHAMADO 
    def tratamento_texto_pld_cc(self):
        self.retorna_data()
        texto_word_etapa1 = f'''
        RESTRITO - As informações contidas nas diligências de PLD/FT são extremamente sigilosas,
        não cabendo a ciência aos Cooperados, envolvidos, terceiros ou intervenientes. Reforçamos
        que os dados devem ser mantidos e armazenados somente no Sistema de PLD/FT, em virtude da 
        Lei Geral de Proteção dos Dados - LGPD. IMPORTANTE: Relembramos o Pacto de Ética Sicoob no item 3.3, 
        aborda o tema CONFLITO DE INTERESSE, determina que: Empregados/Dirigentes do Sicoob NÃO devem intervir
        na tratativa ou decisão de assuntos que envolvam interesses particulares. Prezado(a) gerente! 
        Informamos que o cooperado abaixo, foi alertado (a) no sistema PLD/FT a respeito da divergência
        entre a movimentação e a renda/faturamento. 
        
        *
        *
        *
        *-> A resposta dever ser enviada impreterivelmente até {self.data_inicial}
        
        
        
        '''
        texto_word_etapa2 = '''QUESTIONÁRIO:

        Questão 01:
        Utilizando o princípio conheça seu cooperado, explique quem é o associado alertado, qual a sua área de atuação, fluxo de renda e forneça informações que nos ajude a entender a sua movimentação.

        Questão 02: 
        Explique os principais créditos e débitos ocorridos no mês em questão, bem como suas respectivas origens e destinos. 

        Questão 03:
        Qual a justificativa para a movimentação acima da capacidade declarada em cadastro?

        Questão 04:
        O gerente possui informações de algum fato adicional que agregue a sua resposta? Caso positivo, relatar o fato detalhadamente.

        -------------------------------------------------------------------------------------------------------------------- 
        IMPORTANTE: 
        - Para as respostas que tenham comprovação documental, os documentos devem ser anexados nesta ocorrência (aba anexo) para compor o dossiê digital.
        - Vale destacar, que as respostas não conclusivas prejudicam as diligências e podem ser marcadas na Plataforma PLD/FT como *"INSUFICIÊNCIA da aplicação do princípio conheça seu cooperado/cliente", que pode ser considerado elegível para comunicação ao BCB, conforme descrito na Política Institucional de Fatos Relevantes do Sicoob. 
        - Destacamos que a aplicação do princípio conheça seu cooperado/cliente é regulada pelo Comitê Basiléia e Circular Bacen nº 3.978/2020.
        - As informações prestadas pelo gerente responsável pela conta, subsidiam a recomendação de finalização da ocorrência com ou sem comunicação ao COAF, consideramos, que as informações inseridas na resposta do questionário, serão checadas, analisadas e verdadeiras.
   
        '''
        self.texto_pld = self.texto_pld
        inicio = self.texto_pld.find('RESTRITO')
        fim = self.texto_pld.find('- A seguir')
        self.texto_etapa_um = self.texto_pld[inicio] + self.texto_pld[fim:]
        posicao_importante = self.texto_etapa_um.find('IMPORTANTE:')
        self.texto_etapa_dois = self.texto_etapa_um[:posicao_importante]
        posicao_situacao = self.texto_etapa_dois.find('*Situações')
        parte_cortada = self.texto_etapa_dois[posicao_situacao:]
        parte_inicial = self.texto_etapa_dois[:posicao_situacao]
        self.texto_etapa_tres = parte_cortada + parte_inicial
        self.texto_etapa_quatro = texto_word_etapa1 + self.texto_etapa_tres
        self.texto_etapa_cinco = self.texto_etapa_quatro + texto_word_etapa2
        print(f'Esse é o texto?:  {self.texto_etapa_cinco}')

    # FUNÇÃO QUE RETORNA PARA O BROWSER 
    def retorna_browser(self):
        self.img_browser_aberto = py.locateOnScreen('img/browserAberto.png', confidence=0.9)
        if (self.img_browser_aberto is None):
            print('Browser não está aberto')
        else:
            self.posicao_browser = py.center(self.img_browser_aberto)
            py.moveTo(self.posicao_browser)
            py.click()

    # FUNÇÃO QUE ALTERA AS ABAS DA PÁGINA
    def alt_pagina(self):
        py.time.sleep(1)
        py.hotkey('ctrl', 'tab')

    # FUNÇÃO QUE ACESSA A PÁGIAN DE CHAMADOS
    def acessar_chamados(self):
        py.time.sleep(1.5)

        while True:
            self.imgBtGLPI = py.locateOnScreen('img/inicialIntranet.png', confidence=0.9)
            if (self.imgBtGLPI is None):
                print('Bt não encontrado')
                py.time.sleep(1)
            else:
                py.time.sleep(1)
                self.posicaoBtGLPI = py.center(self.imgBtGLPI)
                py.moveTo(self.posicaoBtGLPI)
                py.click()
                break

    # FUNÇÃO QUE ACESSA A ABERTURA DE NOVOS CHAMADOS 
    def novo_chamado(self):
            while True:
                self.img_abrir_chamado = py.locateOnScreen('img/abrirChamado.png', confidence=0.9)
                if (self.img_abrir_chamado is None):
                    py.time.sleep(1)
                else:
                    py.time.sleep(1.5)
                    py.press('tab', presses=34)
                    py.time.sleep(1.5)
                    py.press('enter')
                    break

    # FUNÇÃO QUE SELECIONA O SETOR
    def select_setor(self):
        while True:
            self.img_tela_abertura = py.locateOnScreen('img/telaAbertura.png', confidence=0.9)
            if (self.img_tela_abertura is None):
                py.time.sleep(1)
            else:
                py.time.sleep(2)
                py.press('tab', presses=34)
                py.time.sleep(1.9)
                py.press('enter')
                py.time.sleep(1.7)
                py.press('down', presses=12)
                py.time.sleep(1.5)
                py.press('enter')
                break

    # FUNÇÃO QUE Selecione o Departamento do Chamado
    def select_departamento(self):
        while True:
            self.img_departamento = py.locateOnScreen('img/departamento.png', confidence=0.9)
            if (self.img_departamento is None):
                py.time.sleep(1)
            else:
                self.posicao_departamento = py.center(self.img_departamento)
                py.moveTo(self.posicao_departamento)
                py.click()
                break
        
        py.time.sleep(2)
        py.press('tab', presses=3)
        py.time.sleep(1.5)
        py.press('enter')
    
    # FUNÇÃO QUE PREENCHER O FORMULARIO PARA ABERTURA DO CHAMADO 
    def preenche_form(self):
        self.get_dados_cooperado()
        while True:
            self.img_form = py.locateOnScreen('img/form.png', confidence=0.9)
            if (self.img_form is None):
                py.time.sleep(1)
            else:
                # ETAPA SELEICONANDO PLD/FT 
                py.time.sleep(1.5)
                py.press('tab', presses=2)
                py.time.sleep(1)
                py.press('enter')
                py.time.sleep(1.1)
                py.press('down')
                py.time.sleep(1.1)
                py.press('enter')

                # ETAPA PREENCHENDO ID OCORRENCIA 
                py.time.sleep(1.1)
                py.press('tab')
                py.time.sleep(0.9)
                py.write(self.numero_ocorrencia.group(1))

                # ETAPA PREENCHENDO O NOME DO COOPERADO 
                py.time.sleep(0.9)
                py.press('tab')
                py.write(self.nome_cooperado)

                # ETAPA PREENCHENDO O PA DO COOPERADO 
                py.time.sleep(0.9)
                py.press('tab')
                py.write(self.pa)

                # ETAPA PREENCHENDO A DESCRICAO DO CHAMADO COM O TEXTO PLD MONTADO 
                py.time.sleep(0.9)
                py.press('tab')
                pyperclip.copy(self.texto_etapa_cinco)
                py.hotkey('ctrl', 'v')
                py.time.sleep(1.5)
                break

    # FUNÇÃO QUE RECUPERA O CPF/CNPJ DO COOPERADO EM QUESTÃO 
    def get_cnpj_cpf(self):
        self.cpf_cnpj_cooperado = ''
        py.time.sleep(2.2)
        py.press('tab', presses=8)
        py.time.sleep(1.2)
        py.hotkey('ctrl', 'c')
        self.cpf_cnpj_cooperado_bruto = pyperclip.paste()
        self.cpf_cnpj_cooperado = re.sub('[^0-9]', '', self.cpf_cnpj_cooperado_bruto)
        py.time.sleep(1.5)
        self.fechar_janelas()
        print(f'Esse é o cpf:? {self.cpf_cnpj_cooperado}')

    # FUNÇÃO QUE RECUPERA OS DADOS DO COOPERADO VIA API 
    def get_dados_cooperado(self):
        self.nome_cooperado = ''
        py.time.sleep(2)
        request = rq.get(f'http://10.54.56.51:8000/api/cooperado/{self.cpf_cnpj_cooperado}')
        resposta = request.json()

        if 'id' in resposta:
            print(resposta)
            self.nome_cooperado = resposta['nome']
            self.pa = resposta['pa']
            self.gerente = resposta['gerente']

        else:
            print('Cooperado não encontrado')

    # FUNÇÃO QUE CLICKA NO BUTÃO ABRIR CHAMADO 
    def click_abri_chamado(self):
        py.time.sleep(1.5)
        py.hscroll(-100000)
        py.time.sleep(1.5)
        while True:
            self.img_bt_chamado = py.locateOnScreen('img/abrirChamadoFato.png', confidence=0.9)
            if (self.img_bt_chamado is None):
                py.time.sleep(1)
            else:
                self.posicao_novo_chamado = py.center(self.img_bt_chamado)
                py.moveTo(self.posicao_novo_chamado)
                py.click()
                break
        while True:
            self.bt_ok = py.locateOnScreen('img/btOk.png', confidence=0.9)
            if (self.bt_ok is None):
                py.time.sleep(1)
            else:
                py.press('enter')
                break

    # FUNÇÃO QUE ACESSA O CHAMADO 
    def acessar_chamado_aberto(self):
        while True:
            self.imgBtNovoChamado = py.locateOnScreen("img/abrirChamado.png", confidence=0.9)
            if (self.imgBtNovoChamado is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1.5)
                py.press('tab', presses=46)
                py.time.sleep(1)
                py.press('enter')
                break

    # FUNÇAO QUE VALIDA SE EXISTE UM GERENTE VINCULADO A CONTA, SE NÃO A AUTOMAÇÃO IRA ADICIONAR QUALQUER UM DA GERÊNCIA 
    def analisa_gerente(self):
        print("Analisa gerente")
        if (self.gerente == 'NÃO INFORMADO'):
            print('Devemos adicionar alguem da gerência')
            self.cargo_gerente = py.locateOnScreen('img/cargoGerente.png', confidence=0.9)
            self.posicao_gerente = py.center(self.cargo_gerente)
            py.moveTo(self.posicao_gerente)
            py.click()
        else:
            py.write(self.gerente)
            py.time.sleep(0.9)
            py.press('enter')


    # FUNÇÃO QUE ALTERA O STATUS DO CHAMADO E VINCULA O GERENTE 
    def vinculo_gerente(self):
        while True:
            self.img_vinculo_gerente = py.locateOnScreen('img/imgVinculoGerente.png', confidence=0.9)
            if (self.img_vinculo_gerente is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1)
                py.press('tab', presses=35)
                py.time.sleep(1.1)
                py.press('enter')
                py.time.sleep(1.5)
                py.press('down', presses=9)
                py.time.sleep(1)
                py.press('enter')
                break
        while True:
            self.confirma = py.locateOnScreen('img/confirmaVinculo.png', confidence=0.9)
            if (self.confirma is None):
                py.time.sleep(1)
            else:
                py.press('tab', presses=2)
                py.time.sleep(1)
                py.press('enter')
                break
        while True:
            self.img_bt_ok = py.locateOnScreen('img/btOk.png', confidence=0.9)
            if (self.img_bt_ok is None):
                py.time.sleep(1)
            else:
                py.press('tab')
                py.press('enter')
                break
        # ETAPA DO VINCULO DE GERENTE 
        while True:
            self.img_vinculo_gerente = py.locateOnScreen('img/imgVinculoGerente.png', confidence=0.9)
            if (self.img_vinculo_gerente is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1.1)
                py.press('tab', presses=37)
                py.time.sleep(1)
                py.press('enter')
                break
        while True:
            self.img_sem_vinculo = py.locateOnScreen('img/semVinculo.png', confidence=0.9)
            if (self.img_sem_vinculo is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1.1)
                py.press('tab', presses=4)
                py.time.sleep(1.1)          
                py.press('enter')
                break

        while True:
            self.img_add_gerente = py.locateOnScreen('img/addGerente.png', confidence=0.9)
            if (self.img_add_gerente is None):
                py.time.sleep(1)
            else:
                py.time.sleep(0.8)
                py.press('tab', presses=2)
                py.time.sleep(1)
                py.press('enter')
                py.time.sleep(1)
                py.press('down', presses=2)
                py.time.sleep(1)
                py.press('enter')
                py.time.sleep(1.5)
                py.press('tab')
                py.time.sleep(0.9)
                # py.press('enter')
                # py.time.sleep(1)
                # py.write(f'pa {self.pa}')
                # py.press('enter')
                # py.time.sleep(1)
                # py.press('tab')
                # py.time.sleep(0.8)
                # py.press('enter')
                # py.time.sleep(0.6)
                py.write(self.gerente)
                py.time.sleep(1)
                py.press('tab', presses=2)
                py.time.sleep(1)
                py.press('enter')
                break

        while True:
            self.img_ok = py.locateOnScreen('img/btOk.png', confidence=0.9)
            if (self.img_ok is None):
                py.time.sleep(1)
            else:
                py.press('enter')
                break

    # FUNÇÃO QUE PEGA O NUMERO DO CHAMADO 
    def get_numero_chamado(self):
        py.time.sleep(1.5)
        py.hotkey('ctrl', 'l')
        py.hotkey('ctrl', 'c')
        self.url_chamado = pyperclip.paste()
        self.url_fatiado = self.url_chamado.strip()
        self.numero_chamado = self.url_fatiado[-6:]
        py.time.sleep(1.5)
        py.hotkey('ctrl', 'w')
        py.time.sleep(2)
        pyperclip.copy('https://intranet.sicoobaracoop.com.br/ ')
        py.hotkey('ctrl', 'l')
        py.hotkey('ctrl', 'v')
        py.press('enter')
        print(f'a {self.numero_chamado}')

    # FUNÇÃO QUE PEGA O NÚMERO DO GERENTE VIA API 
    def get_numero_gerente(self):
        self.dados_gerente = rq.get(f'http://10.54.56.51:8000/api/gerentes/{self.pa}/{self.gerente}')
        if (self.dados_gerente.status_code == 200):
            resposta = self.dados_gerente.json()
            numero_gerente = resposta['mensagem']['celular']
            retirando = numero_gerente.maketrans("", "", string.punctuation)
            self.numero_celular_gerente = numero_gerente.translate(retirando)
            self.iniciar_conversa()
            self.mensagem()
        elif(self.dados_gerente == 404):
            print('Os dados do gerente não foi encontrado na base da API')
            pass

    # FUNÇÃO QUE ABRE UM CHAT NO WATSAPP 
    def iniciar_conversa(self):
        pyperclip.copy(f'https://web.whatsapp.com/send?phone=55{self.numero_celular_gerente}')
        py.hotkey('ctrl', 't')
        py.hotkey('ctrl', 'l')
        py.hotkey('ctrl', 'v')
        py.time.sleep(1)
        py.press('enter')

    # FUNÇÃO QUE IRA ESCREVER E ENVIAR A MESANGEM 
    def mensagem(self):
        while True:
            self.img_whats = py.locateOnScreen('img/inicialWat.png', confidence=0.9)
            if (self.img_whats is None):
                py.time.sleep(1)
            else:
                py.time.sleep(1.5)
                pyperclip.copy(f"Ola! Voce possui um chamado GLPI  #{self.numero_chamado}, assunto PLD-FT, pendente de interacao. Prazo para retorno no GLPI: {self.data_inicial}.")
                py.hotkey('ctrl', 'v')
                py.time.sleep(0.9)
                py.press('enter')
                py.time.sleep(1.5)
                py.hotkey('ctrl', 'w')
                py.press('enter')
                break

    # FUNÇÃO QUE É CHAMADA QUANDO UMA RODADA DE ABERTURA É FINALIZADA
    def fim(self):
         data = {
              "mensagem": f"Foi aberto um novo chamado PLDF/FT ID {self.numero_chamado} - Cooperado(a): {self.nome_cooperado}",
              "robo_id": "1",
              "protocolo": f"{self.numero_chamado}"
         }
         resposta = rq.post('http://10.54.56.51:8000/api/servico', json=data)
         print(resposta)