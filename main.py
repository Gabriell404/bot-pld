import metodos

import time
import execption
erro = execption.Exception()
a = metodos.Metodos()

class Main:
    def bloco(self):
        a.abrir_browser()
        a.analisa_carregamento_browser()
        a.acessar_sites()
        a.acessar_pasta_pld()
        try:
            while True:
                a.att_pasta_pld()
                a.analisa_pasta_pld()
                a.acessar_email()
                a.get_texto_email()
                a.get_numero_ocorrencia()
                a.acessar_sisbr()
                a.pesquisar_pld()
                a.acessar_painel_analise_ocorrencia()
                a.insert_campo_id()
                a.press_pesquisar()
                a.existe_ocorrencia()
                a.press_analissar()
                a.acessar_analises()
                a.acessar_primeiro_registro_analises()
                a.get_texto_pld()
                a.tratamento_texto_pld()
                a.get_cnpj_cpf()    
                a.retorna_browser() 
                a.alt_pagina()          
                a.acessar_chamados()
                a.novo_chamado()
                a.select_setor()
                a.select_departamento()
                a.preenche_form()
                a.click_abri_chamado()
                a.acessar_chamado_aberto()
                a.vinculo_gerente()
                a.get_numero_chamado()
                # a.get_numero_gerente()
                a.alt_pagina()
                a.fim()
                time.sleep(1.5)
        except Exception as e:
            erro.erro_generico(e)
b = Main()
b.bloco()