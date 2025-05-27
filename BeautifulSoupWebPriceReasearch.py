import pandas as pd
import requests
from bs4 import BeautifulSoup

# Carregar a planilha
archive_up = r'G:\My Drive\T.I\Equipaments 2024.csv'
df_inventario = pd.read_csv(archive_up)


def get_product_price(product_name):
  try:
    # Realiza a busca no Google Shopping
    search_query = product_name.replace(' ', '+')
    url = f'https://www.google.com/search?q={search_query}&tbm=shop'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra o preço do primeiro resultado
    price_element = soup.find('span', {'class': 'HRLxBb'})
    if price_element:
      price = price_element.text
      return price
    else:
      return None
  except:
    return None

df_inventario['current price'] = df_inventario['Item'].apply(get_product_price)

output_file = r'G:\\My Drive\\T.I\\Equipaments 2024 - VS Code 27 05 2025.xlsx'
df_inventario.to_excel(output_file, index=False)
