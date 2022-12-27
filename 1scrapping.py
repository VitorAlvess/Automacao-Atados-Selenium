from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep 
import json
import os

with open("settings_pessoal.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo config com usernames e passwords
    dados = json.load(meu_json)
    email = dados["email"]
    senha = dados["password"]
    acesso = dados["access"]
    print('Dados do settings.json lidos com sucesso!')
options = webdriver.ChromeOptions()
preferences = {"download.default_directory" : f'{os.getcwd()}\\relatorios', 'profile.default_content_setting_values.automatic_downloads': 1}
options.add_experimental_option("prefs", preferences)
servico = Service(ChromeDriverManager().install())
navegar = webdriver.Chrome(service=servico, chrome_options=options)



pagina = navegar
pagina.maximize_window()
pagina.get('https://www.atados.com.br/ong/pipa')
pagina.find_element('xpath',' //*[@id="toolbar-auth-button"]' ).click()

if acesso == 'mail':
    print('Metodo de login: mail')
    pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[1]' ).click()
    pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[2]/input' ).send_keys(email)
    pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/div[3]/input' ).send_keys(senha)
    pagina.find_element('xpath',' /html/body/reach-portal/div[3]/div/div/div/form/div/button' ).click()

elif acesso == 'google':  
    print('Metodo de login: Google')
    pagina.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div/div[1]/div/button[3]' ).click()
    sleep(5)
    sleep(5)
    wids = pagina.window_handles
    for window in wids:
        pagina.switch_to.window(window)
        if 'google' in pagina.current_url:
            print("Trocando para a página de login do google")
            break
    pagina.find_element('xpath','//*[@id="identifierId"]' ).send_keys(email)
    pagina.find_element('xpath',' //*[@id="identifierNext"]' ).click()
    print('cliquei em next')
    sleep(5)
    pagina.find_element('xpath','//*[@id="password"]/div[1]/div/div[1]/input' ).send_keys(senha)
    pagina.find_element('xpath','//*[@id="passwordNext"]' ).click()
    sleep(5)
    for window in wids:
        pagina.switch_to.window(window)
        if 'atados' in pagina.current_url:
            print('Voltando para a página do Atados')
            break
else:
    print('Por favor Insira no arquivo settings.json uma configuração de access de "mail" ou "google" ')



print('Login Realizado com sucesso!')
print('Página da ONG PiPA')
# pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=') versão correta que vai mostrar vagas ativas é essa
pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=true&query=')

sleep(5) #Arrumar com delay do proprio webdriver
vagas = pagina.find_elements('xpath','//td[@class="pl-5"]//a') #Clica em gerenciar vagas

#Listar vagas
print(f'Total de vagas ativas: {len(vagas)}')
i = 0
while i < len(vagas): 
    
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
        print('Não possui segundo botão')

    # pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=published&query=') versão correta que vai mostrar vagas ativas é essa
    pagina.get('https://www.atados.com.br/ong/pipa/gerenciar/vagas?closed=true&query=')

    sleep(4)
    i = i + 1
sleep(5)