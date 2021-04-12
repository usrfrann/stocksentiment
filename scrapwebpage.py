import requests
from bs4 import BeautifulSoup
import re

def getArticleText(url):
    articleList = []
    URL = url
    cleanr = re.compile('<.*?>')
    cleanb = re.compile('\[|]')
    page = requests.get(URL)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_elem = soup.find_all("div", class_='caas-body')
    for p_elem in div_elem:
        pdata = p_elem.find_all('p')
        articleList.append(pdata)
        #print("\nElement 1: ")
        #print(p_elem)
    articleListString = "".join(str(articleList[0]))
    articleListString = re.sub(cleanr, '', articleListString)
    articleListString = re.sub(cleanb, '\"\"\"', articleListString)
    return articleListString



#print(article)