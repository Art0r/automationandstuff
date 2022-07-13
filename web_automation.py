import os
import pandas as pd
from typing import List
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement

website: str = "https://g1.globo.com/politica/"
chromedriver_path: str = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "chromedriver")

service: Service = Service(executable_path=chromedriver_path)
driver: Chrome = Chrome(service=service)
driver.get(website)


containers: List[WebElement] = driver.find_elements(
    by='xpath', value="//*[@id='bstn-rtcl']/div/div[3]/div/div/div/div/div/div[2]/ol/*")

links: List[str] = []
titles: List[str] = []
for container in containers:
    # post = container.find_element(
    #    by='xpath', value="./section[@class='post-bastian-products__section post-mais-lidas__section']").text
    link: WebElement = container.find_element(
        by='xpath', value="./a").get_attribute('href')
    text: str = container.find_element(by='xpath', value='./a/li/span').text
    links.append(link)
    titles.append(text)

x = {'title': titles, 'link': links}
df = pd.DataFrame(x)
df.to_csv('headlines.csv')

driver.quit()
