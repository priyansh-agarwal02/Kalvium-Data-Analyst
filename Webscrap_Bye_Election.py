import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://results.eci.gov.in/AcResultByeJune2024/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.find_all('div', class_='box-content')

data = []

for div in divs:
    constituency_name = div.find('h3').text if div.find('h3') else ''
    state = div.find('h4').text if div.find('h4') else ''
    ruling_person = div.find('h5').text if div.find('h5') else ''
    party = div.find('h6').text if div.find('h6') else ''
    data.append([constituency_name, state, ruling_person, party])

df = pd.DataFrame(data, columns=['Constituency Name', 'State', 'Ruling Person', 'Party'])

df.to_excel('election_results.xlsx', index=False)

print("Data has been scraped and saved to election_results.xlsx")
