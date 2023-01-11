from bs4 import BeautifulSoup
import requests

artistlist =[]
songlist = []
dic = {}
url = "https://www.ultimate-guitar.com/top/tabs"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
artist = doc.find_all(class_="js-store")
artist_nice= str(artist).split("{&quot;")

for row in artist_nice:
    newline = row[row.find("/tab/"):row.find("&quote")]
    actualsong = newline.split("/")
    if len(actualsong) > 3:
        tempsong=actualsong[3].replace("-"," ").split("chord")
        tempsong2 = tempsong[0].split("tabs")
        tempartist = actualsong[2].replace("-"," ")
        songlist.append(str(tempsong2[0].strip()))
        artistlist.append(str(tempartist))

for x in range(len(songlist)):
    print(str(x+1)+ " " + artistlist[x]+ " - "+ songlist[x])
    dic[artistlist[x]] = songlist[x]
print(dic)
