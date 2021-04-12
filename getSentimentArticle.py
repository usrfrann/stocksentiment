import requests
import scrapwebpage
import pymongo
import getstockcompanyinfo

mongoClient = pymongo.MongoClient('mongodb://localhost:27017')
apiurl = "https://aylien-text.p.rapidapi.com/sentiment"
with open('apikey.txt','r') as reader:
    apikey = reader.read()
headers = {
    'x-rapidapi-key': str(apikey),
    'x-rapidapi-host': "aylien-text.p.rapidapi.com"
}
mydb = mongoClient["stockdatabase"]
stockCol = mydb["stocknews"]
stockList = []
urlList = []
totalSentiment = 0
ip = input("Enter the name of the company you would like a sentiment score for:")
myquery = {"name": ip}
mydoc = stockCol.find(myquery, {"name": 0, "_id": 0})
results = list(mydoc)
if len(results)==0:
    print("Empty Cursor")
    getstockcompanyinfo.getStockInfo(ip)
    mydoc = stockCol.find(myquery, {"name": 0, "_id": 0})
    for x in mydoc:
        stockList.append(x)
else:
    for x in mydoc:
        stockList.append(x)

#print(newsList)
try:
    for idx in range(0, len(stockList[0]['link'])):
        urlList.append(stockList[0]['link'][idx])
except IndexError:
    pass
for url in urlList:
    articleText = scrapwebpage.getArticleText(url)
    querystring = {"text": articleText[0:5000]}
    response = requests.request("GET",apiurl,headers=headers,params=querystring)
    responseJSON = response.json()
    totalSentiment += responseJSON['polarity_confidence']

avgSent = totalSentiment / len(urlList)
print("The Average Sent was: ", avgSent, " for the company ", ip)





#


