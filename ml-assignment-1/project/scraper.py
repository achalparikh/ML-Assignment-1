"""
Python IMDB Top weekly movies web scraper:
The script scrapes IMDB top weekly movie data and saves it to a CSV file

Author: Achal Parikh
Date: 22-Jan-2018
Course: Machine Learning and Data Science
"""
import requests
from bs4 import BeautifulSoup
import pandas

#pull all html data from the requested link
request = requests.get("http://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht_1")
#initialize beautiful soup object for parsing received html data
soup = BeautifulSoup(request.text, "html5lib")

#grab information table using inside the "tbody" tag
tableData = soup.find("tbody")

dataList = []
dataDir = {}

#loop through each table row and grab information
for tr in tableData.find_all("tr"):

    title = tr.find("td", {"class":"titleColumn"}).find("a")
    weekendEarning = tr.find("td", {"class":"ratingColumn"})
    overallEarning = tr.find("span", {"class":"secondaryInfo"})
    weeks = tr.find("td", {"class":"weeksColumn"})

    #sting formatting for title and weekend earning
    title = title.text.replace("\n", "").replace(" ", "")
    weekendEarning = weekendEarning.text.replace("\n", "").replace(" ", "")

    #Add data to a list
    dataDir = {"Title": title, "Weekend Earning": weekendEarning, "Overall Earning": overallEarning.text, "Weeks": weeks.text}
    dataList.append(dataDir)

#create pandas dataframe using the list
df = pandas.DataFrame(dataList)
df = df[['Title', 'Weekend Earning', 'Overall Earning', 'Weeks']]

#create a CSV file from cleaned data
df.to_csv("IMDB Box Office Data.csv")
