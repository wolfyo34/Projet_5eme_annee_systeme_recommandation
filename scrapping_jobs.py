from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.careerbuilder.com/jobs?keywords=Computer+&location=usa")
driver.set_window_size(250, 720)
action = ActionChains(driver)

recommended_skills = []
description_tab = []

time.sleep(5)
for i in range(1, 25):
    path_annonce_1 = '/html/body/div[2]/div/div[1]/main/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[3]/div/ol/li['
    path_annonce_2 = ']/a[1]'
    path_annonce = path_annonce_1 + str(i) + path_annonce_2
    driver.find_element_by_xpath(path_annonce).click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 2300);")
    time.sleep(2)
    
    path_description = "jdp_description"

    description = driver.find_element_by_id(path_description)
    time.sleep(2)
    description_tab.append(description.text)

    j = 0
    desc = description_tab[i-1].split("\n")
    a=0
    
    while j <(len(desc)):
        
        if "Help us improve CareerBuilder" in desc[j]:
            a=2
        
        if a==1:
            le_split = desc[j].split(" ")
            recommended_skills.append(le_split)
        
        if "Recommended Skills" in desc[j]:
            a=1
            
        j+=1
    
    time.sleep(2)
    C = {'description': [description_tab[i - 1]], 'competence': [recommended_skills]}
    donnees = DataFrame(C, columns=['description', 'competence'])
    export_csv = donnees.to_csv("jobs.csv", mode='a', index=None, header=False, encoding='utf8', sep=';')
    time.sleep(1)
    driver.execute_script("window.history.go(-1)")
    driver.execute_script("window.scrollTo(0, 800)")
    recommended_skills =[]
    i += 1
    time.sleep(2)
    
    
driver.find_element_by_css_selector("#load_more_jobs > button").click()
time.sleep(5)
print(11)
for i in range(1, 25):
    time.sleep(5)
    path_annonce_1 = ' /html/body/div[2]/div/div[1]/main/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div[3]/div/ol/div/li['
    path_annonce_2 = ']/a[1]'
    path_annonce = path_annonce_1 + str(i) + path_annonce_2
    driver.find_element_by_xpath(path_annonce).click()
    time.sleep(2)
    print(4)

    # path_nom_entreprise = '/html/body/div[2]/div/div[1]/main/div[1]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]'
    # time.sleep(5)
    # nom_entreprise = driver.find_element_by_xpath(path_nom_entreprise)
    print(5)

    driver.execute_script("window.scrollTo(0, 2300);")
    print(6)
    time.sleep(1)

    path_description = "jdp_description"
    print(7)

    description = driver.find_element_by_id(path_description)
    print(8)
    time.sleep(1)
    description_tab.append(description.text)
    print(9) 

    j = 0
    desc = description_tab[i-1].split("\n")
    a=0
    
    while j <(len(desc)):
        
        if "Help us improve CareerBuilder" in desc[j]:
            a=2
        
        if a==1:
            recommended_skills.append(desc[j])
        
        if "Recommended Skills" in desc[j]:
            a=1
            
        j+=1
    
    time.sleep(2)
    C = {'description': [description_tab[i - 1]], 'competence': [recommended_skills]}
    donnees = DataFrame(C, columns=['description', 'competence'])
    export_csv = donnees.to_csv("jobs.csv", mode='a', index=None, header=False, encoding='utf8', sep=';')
    time.sleep(1)
    
    print(7)
    driver.execute_script("window.history.go(-1)")
    driver.execute_script("window.scrollTo(0, 1600)")
    i += 1
    print(9)
    time.sleep(2)
print(10)

