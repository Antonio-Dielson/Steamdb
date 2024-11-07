from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

driver = webdriver.Chrome()
driver.get('https://steamdb.info/sales/')
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
header_row = soup.select('table.table-sales thead tr')
header = [th.text.strip() for th in header_row[0].find_all('th')]
rows = soup.select('table.table-sales tr.app')[:100]

all_data = []
all_data.append(header)

for row in rows:
    columns = [col.text.strip() for col in row.find_all('td')]
    all_data.append(columns)

driver.quit()
csv_filename = 'steam_dados.csv'


with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(all_data)

