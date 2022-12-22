from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import os
import xlrd
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1bX9c3wwYmEH-1MvjATTBzZjOZyFuLW90DCGiVY9xOkE'
SAMPLE_RANGE_NAME = 'dados!A:I'
creds = None
valores_final = []
valor = []
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
    #Passar valores existentes para a variavel valore
    sheet = service.spreadsheets()


    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
    valores = result['values']

    # Pegar os dados das planilhas voluntarios
    valores_adicionar = []
    valores_total = []
    for i in range(20): # Total de planilhas
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
    # for i in range(len(valores)):
        
    #     valores[i].pop(0)       
    for i in range(len(valores_total)): #Passar os valores que não estão no google sheet
        if valores_total[i] not in valores:
            valores_final.append(valores_total[i])

    sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME, valueInputOption="RAW", body={'values': valores_final}).execute()        
    print(valores_final)
except HttpError as err:
        print(err)
