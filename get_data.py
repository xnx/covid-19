import pandas as pd

# The confirmed cases by country
data_url = ('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
            'csse_covid_19_data/csse_covid_19_time_series'
            '/time_series_covid19_confirmed_global.csv')

df = pd.read_csv(data_url)
df.to_csv('covid-19-cases.csv')

# The number of deaths by country
data_url = ('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/'
            'csse_covid_19_data/csse_covid_19_time_series'
            '/time_series_covid19_deaths_global.csv')

df = pd.read_csv(data_url)
df.to_csv('covid-19-deaths.csv')
