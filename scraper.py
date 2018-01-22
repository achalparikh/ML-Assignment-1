import requests
from bs4 import BeautifulSoup
import pandas

request = requests.get("http://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht_1")
soup = BeautifulSoup(request.text, "html5lib")

tableData = soup.find("tbody")

dataList = []
dataDir = {}
for tr in tableData.find_all("tr"):

    title = tr.find("td", {"class":"titleColumn"}).find("a")
    weekendEarning = tr.find("td", {"class":"ratingColumn"})
    overallEarning = tr.find("span", {"class":"secondaryInfo"})
    weeks = tr.find("td", {"class":"weeksColumn"})

    title = title.text.replace("\n", "").replace(" ", "")
    weekendEarning = weekendEarning.text.replace("\n", "").replace(" ", "")

    dataDir = {"Title": title, "Weekend Earning": weekendEarning, "Overall Earning": overallEarning.text, "Weeks": weeks.text}
    dataList.append(dataDir)

df = pandas.DataFrame(dataList)
df = df[['Title', 'Weekend Earning', 'Overall Earning', "Weeks"]]

df.to_csv("IMDB Box Office Data.csv")
