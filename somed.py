from __future__ import unicode_literals
import pyautogui
import time
import os
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

plitery = "ęóąśłżźćń"
litery = "eoaslzxćn"


lekarze=open('C:\\Users\\Gabinet\\Desktop\\ewusie.txt','r',encoding="utf-8").read().split('\n')

def StartSomed():
    os.startfile("C:\KS\KS-PLW\KSPL.EXE")
    time.sleep(5)
    pyautogui.moveTo(1029, 254, duration=1)
    pyautogui.click()

def LoginGUI(login, password):
    pyautogui.moveTo(489, 645, duration=1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(802, 477, duration=0.5)
    pyautogui.click()
    pyautogui.write(login)
    pyautogui.moveTo(796, 504, duration=0.5)
    pyautogui.click()
    pyautogui.write(password)
    pyautogui.moveTo(881, 601, duration=0.5)
    pyautogui.click()
    time.sleep(2)

def Administrator():
    pyautogui.moveTo(1085, 375, duration=1)
    pyautogui.click()
    pyautogui.moveTo(807, 366, duration=2)
    pyautogui.click()

def NfzSomed():

    for l in lekarze:
        pyautogui.moveTo(730, 679, duration=0.5)
        pyautogui.click()
        for d in l.split("/")[0]:
            if d in plitery:
                d = litery[plitery.index(d)]
                pyautogui.keyDown('altright')
                pyautogui.press(d)
                pyautogui.keyUp('altright')
            else:
                pyautogui.typewrite(d)

        pyautogui.moveTo(1194, 412, duration=0.5)
        pyautogui.click()

        pyautogui.moveTo(739, 523, duration=0.5)
        pyautogui.click()
        pyautogui.click()
        pyautogui.write(l.split("/")[3])

        pyautogui.moveTo(939, 667, duration=0.5)
        pyautogui.click()

def Wskaznik():
    while True:
        time.sleep(1)
        print(pyautogui.position())

def NfzStrona():
    driver = webdriver.Chrome(r'D:\Pobrane\chromedriver_win32\chromedriver.exe')
    driver.get(
        "https://portal.nfz-krakow.pl/CLO.External.IdentityServer/identity/account/login?returnUrl=%2FCLO.External.IdentityServer%2Fidentity%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DCLO_WS_5%26redirect_uri%3Dhttps%253A%252F%252Fportal.nfz-krakow.pl%252FClO_WS%252F%26response_mode%3Dform_post%26response_type%3Dcode%2520id_token%2520token%26scope%3Dopenid%2520profile%2520clo_ws%26state%3DOpenIdConnect.AuthenticationProperties%253DyavOuoVT4NS_NPA_WOinFwe8NJuKc4Kd9OWNZ4Fww0nMGSdnsQ1EUmzyFFaWFLYG8Z2MseFA8FiPEytB4cT8SHILCES2H6jOH_GAkCwY4LqGVXsdGbKHyOk_5fy9FIuUmqEZl7EKx4rsh3YB__D03QveuJmV74BTKCFNxH3_subi-OZxNdUyGZWvEmwByOxvQihKtpNQ7yzyOaR1Q0SW13Z2dpprzMlCft_AMR2WS04%26nonce%3D637423476007627266.ZGE5MTQzYWUtMWFkNy00YTE1LTg3NjYtYTI4YzcwYzdmNmMwY2ViZWFmOGQtOTEyOS00YWNkLTg4MDctMDVhMDk2YjhiYTdj%26x-client-SKU%3DID_NET%26x-client-ver%3D1.0.40306.1554")

    for l in lekarze: #strona admina
        driver.find_element_by_xpath("""//*[@id="code"]""").send_keys("code")
        driver.find_element_by_xpath("""//*[@id="user_id"]""").send_keys("id")
        driver.find_element_by_xpath("""//*[@id="password"]""").send_keys("password")
        driver.find_element_by_xpath("""//*[@id="MainBody"]/div[2]/div/div[2]/div[2]/div/div[2]/form/fieldset/div[5]/div/button""").click()

        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_lbtnAdministracja"]""").click()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtNazwisko"]""").click()
        ActionChains(driver).send_keys(l.split(";")[0]).perform()
        time.sleep(2)
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnWyszukaj"]""").click()
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_gvUzytkownicy_ctl02_lbtnIdentyfikator"]""").click()
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_tbNoweHaslo1"]""").send_keys(l.split("/")[2])
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_tbNoweHaslo2"]""").send_keys(l.split("/")[2])
        time.sleep(1)
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnZmienHaslo"]""").click()

        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnReturn"]""").click()

        driver.find_element_by_xpath("""//*[@id="ctl00_lbWyloguj"]""").click()
        driver.find_element_by_xpath("""//*[@id="MainBody"]/div[2]/div/div[2]/div/a""").click()

        #driver.get("https://portal.nfz-krakow.pl/CLO.External.IdentityServer/identity/account/login?returnUrl=%2FCLO.External.IdentityServer%2Fidentity%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DCLO_WS_5%26redirect_uri%3Dhttps%253A%252F%252Fportal.nfz-krakow.pl%252FClO_WS%252F%26response_mode%3Dform_post%26response_type%3Dcode%2520id_token%2520token%26scope%3Dopenid%2520profile%2520clo_ws%26state%3DOpenIdConnect.AuthenticationProperties%253DyavOuoVT4NS_NPA_WOinFwe8NJuKc4Kd9OWNZ4Fww0nMGSdnsQ1EUmzyFFaWFLYG8Z2MseFA8FiPEytB4cT8SHILCES2H6jOH_GAkCwY4LqGVXsdGbKHyOk_5fy9FIuUmqEZl7EKx4rsh3YB__D03QveuJmV74BTKCFNxH3_subi-OZxNdUyGZWvEmwByOxvQihKtpNQ7yzyOaR1Q0SW13Z2dpprzMlCft_AMR2WS04%26nonce%3D637423476007627266.ZGE5MTQzYWUtMWFkNy00YTE1LTg3NjYtYTI4YzcwYzdmNmMwY2ViZWFmOGQtOTEyOS00YWNkLTg4MDctMDVhMDk2YjhiYTdj%26x-client-SKU%3DID_NET%26x-client-ver%3D1.0.40306.1554")

        driver.find_element_by_xpath("""//*[@id="code"]""").send_keys("065/100193")
        driver.find_element_by_xpath("""//*[@id="user_id"]""").send_keys(l.split("/")[1])
        driver.find_element_by_xpath("""//*[@id="password"]""").send_keys(l.split("/")[2])
        driver.find_element_by_xpath("""//*[@id="MainBody"]/div[2]/div/div[2]/div[2]/div/div[2]/form/fieldset/div[5]/div/button""").click()


        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtActualPassword"]""").send_keys(l.split("/")[2])
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtNewPassword"]""").send_keys(l.split("/")[3])
        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_txtNewPasswordRepeat"]""").send_keys(l.split("/")[3])

        driver.find_element_by_xpath("""//*[@id="ctl00_ContentPlaceHolder1_btnChangePassword"]""").click()

        driver.find_element_by_xpath("""//*[@id="ctl00_lbWyloguj"]""").click()
        driver.find_element_by_xpath("""//*[@id="MainBody"]/div[2]/div/div[2]/div/a""").click()




class Ewus():
    loginSomed = getpass.getpass("Login do Somedu: ").upper()
    password = getpass.getpass("Hasło: ")
    loginySomed = ("login1", "login2", "login3")
    if loginSomed in loginySomed:
        NfzStrona()
        StartSomed()
        LoginGUI(loginSomed, password)
        Administrator()
        NfzSomed()

#Wskaznik()

