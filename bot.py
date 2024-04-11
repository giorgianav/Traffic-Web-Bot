import selenium as se
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random
import csv

#url = input("Enter URL: ")
urls = ["https://stepfwd.today/", "https://stepfwd.today/angel-investors-workshop.html", "https://stepfwd.today/accelerator.html", "https://stepfwd.today/diversityreport.html", "https://stepfwd.today/alumni.html"]
#visits = int(input("How much visitor: "))
visits = 20

options = Options()
ua = UserAgent()
#chrome_path = 'path of chromedriver'
chrome_path = '/Applications/Google Chrome.app'



for i in range(visits):
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    #driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_path)
    #service = Service(executable_path='/Applications/Google Chrome.app')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    #driver.get(url)
    driver.get(" ".join(random.choices(urls)))
    driver.set_window_size(1120, 550)
    time.sleep(random.randint(2,10)) 
    print(driver.current_url)
    print(i)
    with open('traffic3.log', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(["User Agent"])
        writer.writerow(userAgent)