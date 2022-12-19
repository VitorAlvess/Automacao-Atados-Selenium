from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import xlrd
from time import sleep

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1bX9c3wwYmEH-1MvjATTBzZjOZyFuLW90DCGiVY9xOkE'
SAMPLE_RANGE_NAME = 'dados!B:J'
creds = None

valores_adicionar = []

if os.path.exists('token.json'): #necessario pegar esse token la da api do google sheets
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

try:
    service = build('sheets', 'v4', credentials=creds)
    #Passar valores
    sheet = service.spreadsheets()

    workbook = xlrd.open_workbook('relatorios/voluntarios.xls') #Use o nome do seu arquivo
    worksheet = workbook.sheet_by_name('Usuários Inscritos') #Use o nome da aba do seu arquivo
    worksheet = workbook.sheet_by_index(0)

    for i in range(20):
        if i == 0:
            workbook = xlrd.open_workbook('relatorios/voluntarios.xls') #Use o nome do seu arquivo
        else:
            workbook = xlrd.open_workbook(f'relatorios/voluntarios ({i}).xls') #Use o nome do seu arquivo
        worksheet = workbook.sheet_by_name('Usuários Inscritos') #Use o nome da aba do seu arquivo
        worksheet = workbook.sheet_by_index(0)

      
        for linhas in range(worksheet.nrows): 
            if linhas == 0:
                pass
            else:
                for colunas in range(worksheet.ncols): 
                    valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                    valores_adicionar.append(valor) # Insere os valores na lista
                
                print(valores_adicionar)
                result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME, valueInputOption="RAW", body={'values': [valores_adicionar]}).execute()
                sleep(2)
                valores_adicionar = []
               


    # result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                                 range=SAMPLE_RANGE_NAME, valueInputOption="RAW", body={'values': todos_valores}).execute()
        

except HttpError as err:
        print(err)
