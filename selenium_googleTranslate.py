from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
ChromeDriverPath = "chromedriver.exe"
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(Path,options=chrome_options)
started = False
lang = ""

def Translate(text, dest):
    global lang, started
    if (not started or lang!=dest): driver.get("https://translate.google.com/?sl=auto&tl="+dest+"&op=translate")
    lang = dest
    started = True
    tempInput = driver.find_element(By.XPATH,"//textarea")
    if (len(tempInput.text)==0): tempInput.clear()
    tempInput.send_keys(text)
    time.sleep(2)
    return driver.find_elements(By.XPATH,"//span[contains(@jsaction, ' ')]")[1].text
print(Translate("as a matter of fact","fr"))
print(Translate("compendious","ar"))
