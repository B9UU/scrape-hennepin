import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
cookies = {"BIGipServerWebSphere_Prod_HTTPS":"2709594028.47873.0000","JSESSIONID":"0000RKA6LitByvhB7u8-WmGijFu:1b7gpf5tk"}

urls = ['https://www16.co.hennepin.mn.us/pins/addrresult.jsp?house=3540&street=Hennepin+Avenue+S&condo=&ps=100&sr=1&first=true&last=false',
'https://www16.co.hennepin.mn.us/pins/addrresult.jsp?house=3540&street=Hennepin+Avenue+S&condo=&ps=100&sr=1&first=false&last=true']
dataa = list()
for url in urls:
    data = requests.get(url,headers=headers, cookies=cookies)
    parsed = bs(data.content,'html.parser')
    links = parsed.find_all('td',align="left")
    for link in links:
        linko = link.find('a').get('href')
        if linko not in dataa:
            dataa.append(linko)
def parsing(dom,xpath):
    dd = dom.xpath(xpath)
    if len(dd) == 0:
        return ''
    else:
        if dd[0].text is not None:
            return dd[0].text.strip()
        return dd[0].text
all = list()
for urll in dataa:
    data = requests.get(f"https://www16.co.hennepin.mn.us/pins/{urll}",headers=headers, cookies=cookies)
    parsed = bs(data.content,'html.parser')
    dom = etree.HTML(str(parsed))
    print(urll)
    data = {
        'Property ID number': parsing(dom,'/html/body/div[3]/section/div/header/div/div[3]/div[2]/strong'),
        'Address': parsing(dom,'/html/body/div[3]/section/div/header/div/div[4]/div[2]'),
        'Owner name': parsing(dom,'/html/body/div[3]/section/div/header/div/div[10]/div[2]'),
        'Taxpayer name and address': [zob.find('div').text for zob in dom.xpath('/html/body/div[3]/section/div/header/div/div[11]/div[2]')[0].findall('div')],
        'Sale date': parsing(dom,'/html/body/div[3]/section/div/div/article[1]/div[2]/div[2]/div[2]'),
        'Sale price': parsing(dom,'/html/body/div[3]/section/div/div/article[1]/div[2]/div[3]/div[2]'),
        'Estimated market value':parsing(dom,'/html/body/div[3]/section/div/div/article[3]/div[2]/div[2]/div[2]'),
        'Taxable market value':parsing(dom,'/html/body/div[3]/section/div/div/article[3]/div[2]/div[3]/div[2]'),
        'Total improvement amount': parsing(dom,'/html/body/div[3]/section/div/div/article[3]/div[2]/div[4]/div[2]'),
        'Total net tax': parsing(dom,'/html/body/div[3]/section/div/div/article[3]/div[2]/div[5]/div[2]'),
    }
    all.append(data)
    print(data)
ty = pd.DataFrame(all)
ty.to_csv('data.csv',index=False)
