import requests
from bs4 import BeautifulSoup as bs
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

url = 'https://www16.co.hennepin.mn.us/pins/pidresult.jsp?pid=0402824310286'
data = requests.get(url,headers=headers, )
parsed = bs(data.content,'html.parser')
dato = parsed.find_all('div', class_='col')
# for i in dato:
#     if i.text == "Property ID number:":
#         dd = i.find_next_sibling("div")
#         print(dd.text)
dom = etree.HTML(str(parsed))
# dd = dom.xpath('/html/body/div[3]/section/div/header/div/div[11]/div[2]')
# # du = bs(dd,'lxml')
# print(dd[0].itertext('div')[0])

dd = parsed.select_one("body > div.page-wrapper > section > div > header > div > div:nth-child(15)")

def parsing(xpath):
    dd = dom.xpath(xpath)
    if len(dd) == 0:
        return None
    else:
        return dd[0].text

# data = [zob.find('div').text for zob in dom.xpath('/html/body/div[3]/section/div/header/div/div[11]/div[2]')[0].findall('div') if zob is not None]
ddo = [zob.find('div').text for zob in dom.xpath('/html/body/div[3]/section/div/header/div/div[11]/div[2]')[0].findall('div') if zob is not None]
print(ddo)
