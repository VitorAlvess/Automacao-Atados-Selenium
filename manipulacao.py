# from IPython.display import display
# import pandas as pd

# tabela_python = pd.read_excel("relatorios/voluntarios.xls")
# tabela_python2 = pd.read_excel("relatorios/voluntarios (1).xls")

# string = tabela_python.loc[[0]]

# print(string)


import xlrd
lista = []  # Cria a lista vazia
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

    numerar = 0
    for linhas in range(worksheet.nrows): 
        if linhas == 0:
            pass
        else:
            for colunas in range(worksheet.ncols): 
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                lista.append(valor) # Insere os valores na lista
            print(lista)
            lista = []
            numerar = numerar + 1
            print(numerar)
    print('Subindor para o sheets')

