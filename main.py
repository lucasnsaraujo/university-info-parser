import json
from re import sub
from selenium import webdriver
from time import sleep

base_url = "https://aluno.uvv.br/Aluno/Post/"


# OPEN OPTIONS JSON FILE AND GETS ID AND PASSWORD
with open('options.json') as file:
    user_data = json.load(file)
    id = user_data['id']
    password = user_data["password"]

print("[1/] Arquivo aberto com sucesso.\n")


# INICIA O WEBDRIVER E LOGA NO PORTAL UVV

driver = webdriver.Chrome()
driver.get("https://aluno.uvv.br/")
sleep(3)

print("[2/] Browser aberto.\n")

id_form = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/div[1]/input")
id_form.send_keys(id)

print("[3/] Matrícula inserida.\n")

password_form = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/div[2]/input")
password_form.send_keys(password)

print("[4/] Senha inserida.\n")

submit_form = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/form/div[3]/div[1]/button")
submit_form.click()

print("Logado com sucesso. Iniciando for loop...\n")

# WHILE LOOP GOING THROUGH EVERY POST

for index in range(608300, 658858):
    try:


        post_url = base_url + str(index)

        driver.get(post_url)
        sleep(3)

        print("[1/3] Post " + str(index) + " aberto.\n")

        post_title = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[1]/div[1]/h1").text
        post_teacher = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div/div[1]/h4/strong").text
        post_subject = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/ol/li[2]/a").text
        post_subject_url = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/ol/li[2]/a").get_attribute('href')
        
        print(post_title, post_teacher, post_subject, post_subject_url)

        print("[2/3] Dados do post obtidos.\n")
        print("Post " + str(index) + " encontrado. Matéria: " + str(post_subject) + '\n')

        post_dict = {
            "post_title" : post_title,
            "teacher" : post_teacher,
            "subject" : post_subject,
            "subject_url" : post_subject_url,
            "post_url" : post_url
            }

        # UPDATES JSON DATA FILE WITH PARSED INFO
        with open('data.json', 'r+') as file:
             data = json.load(file)
             data.append(post_dict)
             file.seek(0)
             json.dump(data, file)
        
        print("[3/3] Arquivo data atualizado com infos.\n")
        print("Indo para próximo post.\n")
        

        

    except:
        print("ERRO! Post nao encontrado. Indo para o proximo")


print("Programa finalizado.")











#