# stocksentiment
Get the Sentiment of a US based companies for trading information 

getSentimentArticle.py is the main run python file that takes input from the user of a US based company and returns the Sentiment score based on the last couple of news articles. 

The main run file uses getstockcompanyinfo.py to check if the data for the company that is being seached has been cached in the local mongodb database. If the company has not been cached the python file will use the yahoo finance api to get the last news articles and store the infomation in the database 

scrapwebpage.py looks in the local database and returns the urls of the related news articles and then scraps the page for the article text. 

getSentimentArticle.py takes the article text returned by scrapwebpage.py and sends the data to an api that calcs the sentiment. The closer to 1 the better the sentiment. Anything above .5 is postive sentiment. 

This app is mainly for helping when deciding to buy stock from a few options. You can enter the companies in question and then buy the compnay with the highest sentiment score. 
