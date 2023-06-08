import requests
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import etree

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones'
page = urlopen(url)
html_code = page.read().decode('UTF-8')
soup = BeautifulSoup(html_code, 'html.parser')
links = set()
for link in soup.find_all('a'):
    l = link.get('href')
    if l != None and l.startswith('https'):
        links.add(l)
for link in links:
    print(link)


# start = html_code.find('href="') + 6
# end = html_code.find('">More')
# link = html_code[start:end]
# link = r'(https?://\S+)(?=")'
# print(re.findall(link, html_code))
# tree = etree.HTML(html_code)
# print(tree.xpath("/html/body/div/p[2]/a/@href")[0])  # /html/body/div/p[2]/a
