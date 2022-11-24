from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import json

class automacao: 
    def __init__(self):
        servico = Service(ChromeDriverManager().install())
        self.navegar = webdriver.Chrome(service=servico)
    def iniciar(self):
        self.ler_dados_json()
        self.atados()
        

    def ler_dados_json(self):
         with open("settings_pessoal.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo config com usernames e passwords
            dados = json.load(meu_json)
            self.email = dados["email"]
            self.senha = dados["password"]
            self.acesso = dados["access"]

    def atados(self):
        pagina = self.navegar

        pagina.get('https://atados.com.br')
        pagina.maximize_window()
        pagina.find_element('xpath',' //*[@id="toolbar-auth-button"]' ).click()
        if self.acesso == 'mail':
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[1]' ).click()
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[2]/input' ).send_keys(self.email)
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[3]/input' ).send_keys(self.senha)
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/button' ).click()
        elif self.acesso == 'google':
            pagina.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[3]' ).click()
            sleep(5)
            print(pagina.current_window_handle)
            print(pagina.window_handles)
   
            sleep(5)

            pagina.find_element('xpath','//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]').click()
            pagina.find_element('xpath','//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]').send_keys(self.email)


        else:
            print('Por favor Insira no arquivo settings.json uma configuração de access de "mail" ou "google" ')





        sleep(100)
    

start = automacao()
start.iniciar()
