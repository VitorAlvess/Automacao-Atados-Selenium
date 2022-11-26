from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
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
        preferences = {"download.default_directory" : os.getcwd()}
        options.add_experimental_option("prefs", preferences)
        servico = Service(ChromeDriverManager().install())
        self.navegar = webdriver.Chrome(service=servico, chrome_options=options)
        
    def iniciar(self):
        self.atados()    


    def atados(self):
        pagina = self.navegar

        pagina.get('https://www.atados.com.br/ong/pipa')
        pagina.maximize_window() #provavelmente tirar isso depois para passar para o servidor
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
        pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=')
        print('Total de vagas ativas: ')
        pagina.find_element('xpath','//td[@class="pr-5"]//a//span').click() #Clica em gerenciar vagas
        sleep(10)
        pagina.find_element('xpath', '//*[@id="voluntarios"]/div[1]/div[3]/button').click()
        pagina.find_element('xpath', '//*[@id="voluntarios"]/div[1]/div[2]/button').click()
        print('Arquivos Baixados')

        
        # print(pagina.find_element('xpath','//td[@class="pr-5"]//a//span' ))
        # vagas = pagina.find_elements('xpath','//td[@class="pr-5"]//a//span' ) #pegar todas vagas publicadas
        # for vaga in vagas:
        #     print(vaga.text)

# <selenium.webdriver.remote.webelement.WebElement (session="38ce6453ffaa984705c4b3c7eddd1bd1", element="03259417-073f-4cf5-99d2-cd6102832861")>
# <selenium.webdriver.remote.webelement.WebElement (session="38ce6453ffaa984705c4b3c7eddd1bd1", element="51e41fff-dfb6-491c-9392-42fd6d2f869e")>
# <selenium.webdriver.remote.webelement.WebElement (session="38ce6453ffaa984705c4b3c7eddd1bd1", element="6744f985-947e-4da3-8b54-ce2e87edae86")>
# <selenium.webdriver.remote.webelement.WebElement (session="38ce6453ffaa984705c4b3c7eddd1bd1", element="41bb6a01-4444-49b0-8727-9a61bdc729b2")>
# <selenium.webdriver.remote.webelement.WebElement (session="38ce6453ffaa984705c4b3c7eddd1bd1", element="57094919-c292-48b9-9fa8-bc140895b972")>
# <selenium.webdriver.remote.webelement.WebElement (session="38ce6453ffaa984705c4b3c7eddd1bd1", element="7de5ff35-b1a9-415c-8eb8-c5afaa91ff2c")>
        










        sleep(100)
    

start = automacao()
start.iniciar()
