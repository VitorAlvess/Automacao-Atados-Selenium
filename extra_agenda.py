valores_final = [['Danilo Figueiredo da Costaa', 'dci.infoseg@gmail.com', '(11) 95288-4737', '10/07/2022 21:19:41 +0000', 'Expert em Notebook', 'unapplied-by-deactivation', 'Instituo Center Norte', '07/04/1979', 'São Paulo, SP, Brasil'], ['Miriam Aharonovitss', 'miriam.aharonovitz@gmail.com', '(11) 97280-4493', '14/05/2022 01:36:18 +0000', 'Professor(a) de Gramática', 'confirmed-volunteer', 'Atados', '21/01/1991', 'São Paulo, SP, Brasil'], ['', '', '', '', '', '', '', '', '']]


import pandas as pd


nomes = []
emails = []
telefones = []
cargos = []
aniversarios = []

for nome,email,telefone,_,cargo,_,_,birthday,_ in valores_final:
    if nome != '':
        nomes.append(nome)
        emails.append(email)
        telefones.append(telefone)
        cargos.append(cargo)
        aniversarios.append(birthday)

print(nomes, email, telefone, cargos, aniversarios)

  

info = {"Name": nomes, "Given Name": nomes,"Additional Name": "",	"Family Name": "",	"Yomi Name": "","Given Name Yomi": "",	"Additional Name Yomi": "","Family Name Yomi": "",	"Name Prefix": "",	"Name Suffix": "",	"Initials": "",	"Nickname": '',	"Short Name": '',	"Maiden Name": '',	"Birthday": aniversarios,	"Gender": '', "Location": '',	"Billing Information": '',	"Directory Server": '',	"Mileage": '',	"Occupation": '',	"Hobby": '',	"Sensitivity": '',	"Priority": '',	"Subject": '',	"Notes": '',	"Language": '',	"Photo": '',	"Group Membership": '* myContacts',	"E-mail 1 - Type": '*',	"E-mail 1 - Value": email,	"Phone 1 - Type": '',	"Phone 1 - Value": telefones,	"Organization 1 - Type": '',	"Organization 1 - Name": '',	"Organization 1 - Yomi Name": '',	"Organization 1 - Title": cargos, 	"Organization 1 - Department": '',	"Organization 1 - Symbol": '',"Organization 1 - Location": '',	"Organization 1 - Job Description": ''}
df = pd.DataFrame(info)

df.to_csv('contatos.csv')
