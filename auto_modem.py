from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

modem = "http://192.168.1.1/"

driverChrome = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driverChrome))
driver.get(modem)
sleep(1)

driver.find_element(By.ID, "srp_password").send_keys("blablablabla")
sleep(1)
driver.find_element(By.ID, "sign-me-in").click()
sleep(9)
driver.find_element(By.ID, "Wireless").click()
sleep(6)

# driver.find_element(By.XPATH, xpercorso).click()
# sleep(5)

driver.find_element(By.ID, "save-config").click()
sleep(8)

driver.find_element(By.CLASS_NAME, "icon-remove").click()
sleep(9)
driver.find_element(By.CLASS_NAME, "icon-cogs").click()
sleep(8)
driver.find_element(By.ID, "Configurazione").click()
sleep(8)
driver.find_element(By.ID, "btn-system-reboot").click()
sleep(2)

driver.find_element(By.ID, "ok").click()

input()

driver.quit()
