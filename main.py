import json
from re import sub
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
import urllib.parse

base_url = "https://aluno.uvv.br/Aluno/Post/"
error_counter = 0

def login(options, driver):
    driver.get("https://aluno.uvv.br/")
    sleep(3)

    print("[2/4] Browser aberto.\n")

    id_form = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/form/div[1]/input")
    id_form.send_keys(id)

    print("[3/4] Matrícula inserida.\n")

    password_form = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/form/div[2]/input")
    password_form.send_keys(password)

    print("[4/4] Senha inserida.\n")

    submit_form = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/form/div[3]/div[1]/button")
    submit_form.click()

    print("Logado com sucesso. Iniciando for loop...\n")

    return driver


# OPEN OPTIONS JSON FILE AND GETS ID AND PASSWORD
with open('options.json') as file:
    user_data = json.load(file)
    id = user_data['id']
    password = user_data["password"]
    phone_number = user_data["phone_number"]
    callmebot_api_key = user_data["callmebot_api_key"]

print("[1/4] Arquivo aberto com sucesso.\n")

# PEGA O PROGRESSO DO SCRIPT
try:
    with open('save_progress.json') as progress_load_file:
        data = json.load(progress_load_file)
        last_registered_post = str(data['last_registered_post'])
        print('Progresso encontrado. Continuando do post ' + last_registered_post + '\n')

except:
    print('Progresso não encontrado. Começando novamente.\n')

# INICIA O WEBDRIVER E LOGA NO PORTAL UVV

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
login(options, driver)

# WHILE LOOP GOING THROUGH EVERY POST

for index in range((int(last_registered_post) or 608300), 658858):
    try:
        if error_counter >= 10:
            try:
                driver.close()
                driver = webdriver.Chrome(options=options)
                login(options, driver)
                print("Desconectado do portal. Logando novamente...")
            except:
                pass
            finally: 
                error_counter = 0
                print("Contador de erros resetado para zero.")

        post_url = base_url + str(index)

        driver.get(post_url)
        sleep(3)

        print("[1/3] Post " + str(index) + " aberto.\n")

        post_title = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[1]/div[1]/h1").text
        post_teacher = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div[1]/h4/strong").text
        post_subject = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ol/li[2]/a").text
        post_subject_url = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/ol/li[2]/a").get_attribute('href')

        print("[2/3] Dados do post obtidos.\n")
        print("Post " + str(index) + " encontrado. Matéria: " + str(post_subject) + '\n')

        post_dict = {
            "post_id" : str(index),
            "post_title" : post_title,
            "teacher" : post_teacher,
            "subject" : post_subject,
            "subject_url" : post_subject_url,
            "post_url" : post_url,
            }

        # UPDATES JSON DATA FILE WITH PARSED INFO
        with open('data.json', 'r+') as file:
             data = json.load(file)
             data.append(post_dict)
             file.seek(0)
             json.dump(data, file)
        
        print("[3/3] Arquivo data atualizado com infos.\n")

        # SALVAR PROGRESSO DO SCRIPT
        progress = {"last_registered_post" : str(index)}

        with open('save_progress.json', 'w') as progress_file:
            json.dump(progress, progress_file)

        with open('./react-website/website/src/json_formatted.js', 'r+') as json_formatted_file:
            json_formatted_file.write("""export const data = """ + str(data))

        error_counter = 0
        print("Indo para próximo post.\n")
        print("=-" * 20 + '\n')

    except:
        print("ERRO! Post nao encontrado. Indo para o proximo")
        print("=-" * 20 + '\n')
        error_counter += 1



# SENDS A WHATSAPP MESSAGE IF BOT STOPS WORKING

callmebot_message = urllib.parse.quote("O bot da UVV parou de funcionar.")

requests.get("https://api.callmebot.com/whatsapp.php?phone=" + phone_number + "&text=" + callmebot_message + "&apikey=" + callmebot_api_key)

print("Programa finalizado.")
