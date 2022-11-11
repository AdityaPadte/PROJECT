import requests
from bs4 import BeautifulSoup
url="https://www.simplilearn.com/tutorials/excel-tutorial/excel-shortcuts"
r=requests.get(url)
htmlcontent= r.content
print(htmlcontent)
soup=BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify)
paras=soup.find('article',class_='desig_author empty-text').find_all('td')
for p in paras:
    print(p.text) 
