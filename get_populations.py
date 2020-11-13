import pandas as pd
from bs4 import BeautifulSoup
from country_aliases import country_aliases

LOCAL_CSV_FILE = 'covid-19-cases.csv'

data_loc = LOCAL_CSV_FILE
df = pd.read_csv(data_loc)
df.rename(columns={'Country/Region': 'Country'}, inplace=True)
df.index = df['Country']
df.drop('Country', axis=1, inplace=True)

grouped = df.groupby('Country')
df2 = grouped.sum()
df2.rename(index=country_aliases, inplace=True)

article = open('List of countries by population (United Nations) - Wikipedia.html').read()
soup = BeautifulSoup(article, 'html.parser')
table = soup.find_all('table', class_='sortable')[0]

pops = {}
for i, row in enumerate(table.find('tbody').find_all('tr')):
    cells = row.find_all('td')
    country, population = cells[0].text, cells[4].text.replace(',', '')
    try:
        country = country[:country.index('[')]
    except ValueError:
        pass
    if country == 'Burma':
        country = 'Myanmar'
    pops[country.strip()] = int(population)
pops['Kosovo'] = 1.81e6
pops['Diamond Princess'] = 3711

pops = pd.Series(pops, name='Population').astype(int)
pops.index.name = 'Country'
pops.to_csv('country_populations.csv')
