import os

pasta = 'relatorios'  # substitua pelo caminho para a pasta que você quer apagar

# Itera sobre todos os arquivos na pasta e remove cada um
for nome_arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    if os.path.isfile(caminho_arquivo):
        os.remove(caminho_arquivo)