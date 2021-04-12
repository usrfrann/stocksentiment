import pymongo
import requests
mongoClient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = mongoClient["stockdatabase"]
mycol = mydb["stocknews"]


with open("apikey.txt","r") as reader:
    apikey = reader.read()
#ip = str(input("Enter a Stock Name in the US region"))
def getStockInfo(ip):
    stockurlList = []
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"
    querystring = {"q": ip, "region": "US"}
    headers = {
        'x-rapidapi-key': str(apikey),
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    response = requests.get(url,headers=headers,params=querystring)
    responseJSON = response.json()

    for idx in range(0,len(responseJSON['news'])):
        stockurlList.append(responseJSON['news'][idx]['link'])

    stockurlList = [{"name":ip,"link": stockurlList}]
    print(stockurlList)
    x = mycol.insert_many(stockurlList)
    print(x.inserted_ids)