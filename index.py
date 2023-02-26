from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep 
import json
import os

# parte 2
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import xlrd

#parte 3
import os.path


class scrappy:
    def iniciar(self):
        self.configuracoes_atados()
        self.logar()
        self.pagina_opipa()
        self.configuracoes_sheets()
        self.sheets()
        self.people_api()
        self.apagar_arquivos()
    
    def configuracoes_atados(self):
        with open("settings_pessoal.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo config com usernames e passwords
            dados = json.load(meu_json)
            self.email = dados["email"]
            self.senha = dados["password"]
            self.acesso = dados["access"]
            self.email_contacts = ["email_contacts"]
            self.password_contacts = ["password_contacts"]
            print('Dados do settings.json lidos com sucesso!')
        options = webdriver.ChromeOptions()
        # options.add_argument('--disable-gpu')
        # options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--start-maximized')
        # options.add_argument('--disable-setuid-sandbox')




        preferences = {"download.default_directory" : f'{os.getcwd()}\\relatorios', 'profile.default_content_setting_values.automatic_downloads': 1}
        options.add_experimental_option("prefs", preferences)
        servico = Service(ChromeDriverManager().install())
        self.navegar = webdriver.Chrome(service=servico, options=options)
        print('Passou aqui')
    def logar(self):

        pagina = self.navegar
        pagina.set_window_size(1366,768)
        pagina.get('https://www.atados.com.br/ong/pipa')
        pagina.find_element('xpath',' //*[@id="toolbar-auth-button"]' ).click()

        if self.acesso == 'mail':
            print('Metodo de login: mail')
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[1]' ).click()
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[2]/input' ).send_keys(self.email)
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[3]/input' ).send_keys(self.senha)
            pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/button' ).click()

        elif self.acesso == 'google':  
            print('Metodo de login: Google não está funcionando')
            # pagina.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[3]' ).click()
            # sleep(5)
            
            # wids = pagina.window_handles
            # for window in wids:
            #     pagina.switch_to.window(window)
            #     if 'google' in pagina.current_url:
            #         print("Trocando para a página de login do google")
            #         sleep(5)
            #         break
            # pagina.find_element('xpath','//*[@id="Email"]' ).send_keys(self.email)
            # pagina.find_element('xpath',' //*[@id="next"]' ).click()
            # print('cliquei em next')
            # sleep(5)
            # pagina.find_element('xpath','//*[@id="password"]' ).send_keys(self.senha)
            # login = pagina.find_elements('xpath','//div/button' )
            # sleep(5)
            # print(login)
            # login[2].click()
            # # pagina.find_element('xpath','//*[@id="signIn"]').click()
            # sleep(5)
            # for window in wids:
            #     pagina.switch_to.window(window)
            #     if 'atados' in pagina.current_url:
            #         print('Voltando para a página do Atados')
            #         break
        else:
            print('Por favor Insira no arquivo settings.json uma configuração de access de "mail" ou "google" ')
        sleep(5)
        print('Login Realizado com sucesso!')
    
    def pagina_opipa(self):
        pagina = self.navegar
        print('Página da ONG PiPA')
        # pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=') versão correta que vai mostrar vagas ativas é essa
        pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=')

        sleep(5)
        self.vagas = pagina.find_elements('xpath','//td[@class="pl-5"]//a') #Clica em gerenciar vagas

        #Listar vagas
        print(f'Total de vagas ativas: {len(self.vagas)}')
        i = 0
        while i < len(self.vagas): 
            
            sleep(5)
            vaga_nome = pagina.find_elements('xpath','//td[@class="pl-5"]//a')
            print(vaga_nome[i].text)
            vaga = pagina.find_elements('xpath', '//td[@class="pr-5"]//a[@class="btn bg-primary-500 text-white hover:bg-primary-600 hover:text-white px-3 rounded-full"]')
            pagina.execute_script(f"window.scrollTo(0, {i}99)")
            sleep(2)
            vaga[i].click()
            sleep(4)
            pagina.execute_script(f"window.scrollTo(0, 250)")
            sleep(2)
            try:
                pagina.find_element('xpath','//*[@id="voluntarios"]/div[1]/div[2]/button' ).click()
                sleep(2)
            except:
                print('Não possui o primeiro botão')
            
            try:
                pagina.find_element('xpath','//*[@id="voluntarios"]/div[1]/div[3]/button' ).click()
                sleep(2)
            except:
                print()
                
            pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=')

            sleep(4)
            i = i + 1
        sleep(5)

    def configuracoes_sheets(self):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.creds = None
       
        if os.path.exists('token.json'): #necessario pegar esse token la da api do google sheets
           self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())
        
    def sheets(self):
         # The ID and range of a sample spreadsheet.
        SAMPLE_SPREADSHEET_ID = '1bX9c3wwYmEH-1MvjATTBzZjOZyFuLW90DCGiVY9xOkE'
        SAMPLE_RANGE_NAME = 'dados!A:I'
       
        valores_final = []
        valor = []
        try:
            service = build('sheets', 'v4', credentials=self.creds)
            #Passar valores existentes para a variavel valore
            sheet = service.spreadsheets()


            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                            range=SAMPLE_RANGE_NAME).execute()
            valores = result['values']

            # Pegar os dados das planilhas voluntarios
            valores_adicionar = []
            valores_total = []
            for i in range(len(self.vagas)): # Total de planilhas / Range vai ser definido pelo numero total de vagas ativas
                if i == 0:
                    workbook = xlrd.open_workbook('relatorios/voluntarios.xls') #A 0 é especial 
                else:
                    workbook = xlrd.open_workbook(f'relatorios/voluntarios ({i}).xls') #Looping até 19
                worksheet = workbook.sheet_by_name('Usuários Inscritos') #Nome da aba
                worksheet = workbook.sheet_by_index(0)


                for linhas in range(worksheet.nrows): 
                    if linhas == 0:
                        pass
                    else:
                        for colunas in range(worksheet.ncols): 
                            valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                            valores_adicionar.append(valor) # Insere os valores na lista
                    if valores_adicionar == []:
                        pass
                    else:
                        valores_total.append(valores_adicionar)
                        valores_adicionar = []    
            for i in range(len(valores_total)): #Passar os valores que não estão no google sheet
                if valores_total[i] not in valores:
                    valores_final.append(valores_total[i])

            sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                range=SAMPLE_RANGE_NAME, valueInputOption="RAW", body={'values': valores_final}).execute()        
            print(valores_final) #Valores finais.
            self.valores_final = valores_final
        except HttpError as err:
                print(err)

    def apagar_arquivos(self):
        pasta = 'relatorios'  # substitua pelo caminho para a pasta que você quer apagar
        # Itera sobre todos os arquivos na pasta e remove cada um
        for nome_arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
    
    def people_api(self):
        SCOPES = ['https://www.googleapis.com/auth/contacts']
        """Shows basic usage of the People API.
        Prints the name of the first 10 connections.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token2.json'):
            creds = Credentials.from_authorized_user_file('token2.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token2.json', 'w') as token:
                token.write(creds.to_json())

        try:
            #Valores que vão ser recebidos de outro arquivo
            service = build('people', 'v1', credentials=creds)

            #Criar contato
            for valores in self.valores_final:
                if valores[0] == '':
                    break
                contact = service.people().createContact(
                    body={
                    "names": [
                        {
                        "givenName": valores[0],
                        'familyName': ''
                        }
                    ],
                    "emailAddresses": [
                        {
                        "value": valores[1],
                        "type": "work"
                        }
                    ],
                    "phoneNumbers": [
                        {
                        "value": valores[2],
                        "type": "mobile"
                        }
                    ],
                    "organizations": [
                        {
                        "name": "",
                        "title": valores[4]
                        }
                    ]
                    }
                ).execute()
        except HttpError as err:
            print(err)


start = scrappy()
start.iniciar()