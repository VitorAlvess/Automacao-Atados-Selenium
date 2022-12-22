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
SAMPLE_SPREADSHEET_ID = '1g6gY-WqF3e_d2JUm3AJ0ykFgoKKnYPU52XfFdgmkv-U'
SAMPLE_RANGE_NAME = 'dados!A:J'
creds = None
valores_final = []
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
    print(len(valores))
    valores_final = [['valores', 'Uau']]
    
    for i in range(len(valores)):
        print(i)
    # sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                                     range=f'dados!C4:J', valueInputOption="RAW", body={'values': valores_final}).execute()        
except HttpError as err:
        print(err)
