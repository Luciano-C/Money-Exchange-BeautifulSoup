from bs4 import BeautifulSoup
import pandas as pd
import requests

# Trae la página como html
page = requests.get("https://www.moreexchange.cl/tipo-de-cambio-de-divisas-more-exchange/")

soup = BeautifulSoup(page.text, "html.parser")

# Muestra el título sin las etiquetas
# print(soup.title.string)


""" divs = soup.find_all("div")

for item in divs:
    print(item, '\n') """

# table = soup.find_all("table")
# print(table[0])

table = soup.find_all("table")
df =  pd.read_html(str(table))
print(df[0])

a = soup.find_all("a")


for link in a:
    if link.string == "Comprar Divisas":
        print("Comprar en el siguiente link: ", link.get("href"))