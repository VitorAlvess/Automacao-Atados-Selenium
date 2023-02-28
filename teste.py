 
import xlrd

workbook = xlrd.open_workbook(f'relatorios/voluntarios.xls') 
worksheet = workbook.sheet_by_name('Usuários Inscritos') #Nome da aba
worksheet = workbook.sheet_by_index(0)

valores_adicionar= []
valores_total = []
valores_total = []
for linhas in range(worksheet.nrows): 
    if linhas == 0:
        pass
    else:
        for colunas in range(worksheet.ncols): 
            print(colunas)
            if colunas == 0:
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                valores_adicionar.append(valor) # Insere os valores na lista
            if colunas == 1:
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                valores_adicionar.append(valor) # Insere os valores na lista
            if colunas == 2:
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                valores_adicionar.append(valor) # Insere os valores na lista
            if colunas == 3:
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                valores_adicionar.append(valor.split()[0])
            if colunas == 4:
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                valores_adicionar.append(valor) # Insere os valores na lista
            if colunas == 7:
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                valores_adicionar.append(valor) # Insere os valores na lista
            if colunas == 8:
                valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
                valores_adicionar.append(valor) # Insere os valores na lista
            # if colunas == 3:
            #     valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
            #     valores_adicionar.append(valor.split()[0])

            # elif colunas != 5 or colunas != 6:
            #     valor = worksheet.cell_value(linhas, colunas) # Pega os valores do excel
            #     valores_adicionar.append(valor) # Insere os valores na lista
    if valores_adicionar == []:
        pass
    else:
        valores_total.append(valores_adicionar)
        valores_adicionar = []    
        print(valores_total)
['Isabela Gutierrez Costa', 'isabelagutiz@gmail.com', '(11) 95669-0706', '21/02/2023', '21/02/2023 03:15:50 -0300', 'Educador(a) Lanterninha', 'confirmed-volunteer', 'Instituo Center Norte', '16/03/1998', 'São Paulo, SP, Brasil']
[['Isabela Gutierrez Costa', 'isabelagutiz@gmail.com', '(11) 95669-0706', '21/02/2023', '21/02/2023 03:15:50 -0300', 'Educador(a) Lanterninha', 'confirmed-volunteer', 'Instituo Center Norte', '16/03/1998', 'São Paulo, SP, Brasil'], ['Letícia de Jesus Souza', 'letciasouza.me@gmail.com', '(11) 95144-4007', '28/02/2023', '28/02/2023 18:46:12 -0300', 'Educador(a) Lanterninha', 'applied', 'Instituo Center Norte', '12/03/2003', 
'São Paulo, SP, Brasil']]

[['Isabela Gutierrez Costa', 'isabelagutiz@gmail.com', '(11) 95669-0706', '21/02/2023', '21/02/2023 03:15:50 -0300', 'Educador(a) Lanterninha', 'confirmed-volunteer', 'Instituo Center Norte', '16/03/1998', 'São Paulo, SP, Brasil']]
[['Isabela Gutierrez Costa', 'isabelagutiz@gmail.com', '(11) 95669-0706', '21/02/2023', '21/02/2023 03:15:50 -0300', 'Educador(a) Lanterninha', 'confirmed-volunteer', 'Instituo Center Norte', '16/03/1998', 'São Paulo, SP, Brasil'], ['Letícia de Jesus Souza', 'letciasouza.me@gmail.com', '(11) 95144-4007', '28/02/2023', '28/02/2023 18:46:12 -0300', 'Educador(a) Lanterninha', 'applied', 'Instituo Center Norte', '12/03/2003', 
'São Paulo, SP, Brasil']]