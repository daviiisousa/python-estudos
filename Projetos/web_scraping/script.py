import requests
# pyrefly: ignore [missing-import]
from bs4 import BeautifulSoup


def get_frases():
    url = "https://quotes.toscrape.com/"

    frases_list = []

    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    frases = soup.find_all("span", itemprop="text")
    
    for frase in frases:
        frases_list.append(frase.get_text())

    return frases_list
