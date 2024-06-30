import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

card_headers = soup.find_all('div', class_='card-header')
for header in card_headers:
    if 'Party Wise Results Status' in header.text:
        card_body = header.find_next_sibling('div', class_='card-body')
        table = card_body.find('table')
        break

data = []
rows = table.find_all('tr')
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

columns = ['Party', 'Won', 'Leading', 'Total']
df = pd.DataFrame(data, columns=columns)
df.to_csv('party_results.csv', index=False)

print("Data scraped and saved to party_results.csv")
