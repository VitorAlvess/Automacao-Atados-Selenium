from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv
import os

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1bX9c3wwYmEH-1MvjATTBzZjOZyFuLW90DCGiVY9xOkE'
SAMPLE_RANGE_NAME = 'dados!A:I'
creds = None

valor = ['Renan Mendes', 'renanmendescontact@gmail.com', '(11) 97722-6679', '13/06/2022 04:13:50 +0000', 'Expert em Notebook', 'unapplied-by-deactivation', 'Atados', '08/01/1998']
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


    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
    
    valores = result['values']
   
    
    for i in range(len(valores)):
        print(i)
        valores[i].pop(0)
        print(valores[i])
        if valores[i] == valor:
            break
            
        
    
except HttpError as err:
        print(err)
