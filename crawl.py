from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless') 
browser = webdriver.Chrome(options=options)

url = "https://www.olx.com.br/imoveis/venda/estado-sc/florianopolis-e-regiao?pe=500000&ps=20000&sf=1"
browser.get(url)

time.sleep(5)
soup = BeautifulSoup(browser.page_source, 'html.parser')
elements = soup.find_all()

summary = {
    'total_elements': len(elements),
    'unique_tags': list(set([e.name for e in elements])),
}

print(f"Total elements found: {summary['total_elements']}")
print(f"Unique tags on the page: {summary['unique_tags']}")

import ipdb; ipdb.set_trace()