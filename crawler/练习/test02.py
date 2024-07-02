import requests
from lxml import etree
url = 'https://search.dangdang.com/?key=%D7%F7%BC%D2%B3%F6%B0%E6%C9%E7&category_path=01.05.16.00.00.00#J_tab'

etree.HTML(url)
response = requests.get(url)
print(response.text)