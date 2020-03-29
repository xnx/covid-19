# get_country_populations.py
"""
Get a CSV file of country populations using the same naming conventions as the
Johns Hopkins / CSSE COVID-19 dataset.
"""

import pandas as pd
from country_aliases import country_aliases

# This is the URL to the Wikipedia page for country populations we will use:
url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
# The table we're interested in is the first one read in from the webpage.
df = pd.read_html(url)[0]

# Rename the relevant column to something more manageable.
df.rename(columns={'Country (or dependent territory)': 'Country'}, inplace=True)
# Get rid of the footnote indicators, "[a]", "[b]", etc.
df['Country'] = df['Country'].str.replace('\[\w\]', '')
# Set the 'Country' column to be the index.
df.index = df['Country']

# Our local copy of the COVID-19 cases file.
LOCAL_CSV_FILE = 'covid-19-cases.csv'
df2 = pd.read_csv(LOCAL_CSV_FILE)
# Get the unique country names.
jh_countries = df2['Country/Region'].unique()

with open('country_populations.csv', 'w') as fo:
    print('Country, Population', file=fo)
    for country in jh_countries:
        # If a country named in the CSSE dataset isn't in our populations table
        # then look it up in the aliases dictionary ...
        if country not in df.index:
            try:
                country = country_aliases[country]
            except KeyError:
                # ... if we can't find it in the aliases, skip it.
                print('Skipping', country)
                continue
        # Write the country and its population to the CSV file.
        print('"{}", {}'.format(country, df.at[country, 'Population']),
              file=fo)

