from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import json
import os

class automacao: 
    def __init__(self):
        with open("settings_pessoal.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo config com usernames e passwords
            dados = json.load(meu_json)
            self.email = dados["email"]
            self.senha = dados["password"]
            self.acesso = dados["access"]
            print('Dados do settings.json lidos com sucesso!')
        options = webdriver.ChromeOptions()
        preferences = {"download.default_directory" : os.getcwd()+ '/Relatorios', 'profile.default_content_setting_values.automatic_downloads': 1}
        options.add_experimental_option("prefs", preferences)
        servico = Service(ChromeDriverManager().install())
        self.navegar = webdriver.Chrome(service=servico, chrome_options=options)
        
    def iniciar(self):
        self.atados()    


    def atados(self):
        pagina = self.navegar
        pagina.maximize_window()
        pagina.get('https://www.atados.com.br/ong/pipa')
        pagina.find_element('xpath',' //*[@id="toolbar-auth-button"]' ).click()
        if self.acesso == 'mail':
            print('Metodo de login: mail')
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[1]' ).click()
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[2]/input' ).send_keys(self.email)
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[3]/input' ).send_keys(self.senha)
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/button' ).click()
        elif self.acesso == 'google':  
            print('Metodo de login: Google')
            pagina.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[3]' ).click()
            sleep(5)
            sleep(5)
            wids = pagina.window_handles
            for window in wids:
                pagina.switch_to.window(window)
                if 'google' in pagina.current_url:
                    print("Trocando para a página de login do google")
                    break
            pagina.find_element('xpath','//*[@id="identifierId"]' ).send_keys(self.email)
            pagina.find_element('xpath',' //*[@id="identifierNext"]' ).click()
            print('cliquei em next')
            sleep(5)
            pagina.find_element('xpath','//*[@id="password"]/div[1]/div/div[1]/input' ).send_keys(self.senha)
            pagina.find_element('xpath','//*[@id="passwordNext"]' ).click()
            sleep(5)
            for window in wids:
                pagina.switch_to.window(window)
                if 'atados' in pagina.current_url:
                    print('Voltando para a página do Atados')
                    break
        else:
            print('Por favor Insira no arquivo settings.json uma configuração de access de "mail" ou "google" ')

        print('Login Realizado com sucesso!')
        print('Página da ONG PiPA')
        # pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=') versão correta que vai mostrar vagas ativas é essa
        pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=true&query=')

        sleep(5) #Arrumar com delay do proprio webdriver
        vagas = pagina.find_elements('xpath','//td[@class="pl-5"]//a') #Clica em gerenciar vagas
        
        #Listar vagas
        print(f'Total de vagas ativas: {len(vagas)}')
        i = 0
        while i < len(vagas): 
            pagina.execute_script("document.body.style.zoom='33%'")
            sleep(5)
            vaga_nome = pagina.find_elements('xpath','//td[@class="pl-5"]//a')
            print(vaga_nome[i].text)
            vaga = pagina.find_elements('xpath', '//td[@class="pr-5"]//a[@class="btn bg-primary-500 text-white hover:bg-primary-600 hover:text-white px-3 rounded-full"]')
            vaga[i].click()
            sleep(10)
            # pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=') versão correta que vai mostrar vagas ativas é essa
            pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=true&query=')

            sleep(4)
            i = i + 1
        sleep(5)
    

start = automacao()
start.iniciar()

