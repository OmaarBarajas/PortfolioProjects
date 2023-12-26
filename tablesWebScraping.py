from bs4 import BeautifulSoup
import requests
import pandas as pd

url = ''

#Using module 'Requests' to contact the url.
page = requests.get(url)

#Using BS to obtain the HTML information from the page.
soup = BeautifulSoup(page.text, 'html.parser')

#Looking for the table that we require
table = soup.find_all('table')[1]

#Selecting the table titles from the selected table
world_titles = table.find_all('th')

#Cleaning the formats from the headers
world_table_titles = [title.text.strip() for title in world_titles]

df = pd.DataFrame(columns= world_table_titles)

#Obtaining the rows from the selected table
column_data = table.find_all('tr')

#Assigning values to each row
for row in column_data[1:]:
    row_data = row.find_all('td')

#Assigning values to each cell
    cell_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = cell_data

df.to_csv(r'C:\Users\Omar\Desktop\Python scripts\scrapingtest.csv', index= False)
