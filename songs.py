from bs4 import BeautifulSoup
import requests

artistname = ""
songname = ""
artistlist =[]
songlist = []
dic = {"artist":"","song":""}
url = "https://www.ultimate-guitar.com/top/tabs"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
artist = doc.find_all(class_="js-store")
artist_nice= str(artist).split("{&quot;")
#print(artist)
#print(artist_nice)
#print(doc.prettify())

for row in artist_nice:
    newline = row[row.find("/tab/"):row.find("&quote")]
    # print(newline[5:])
    actualsong = newline.split("/")
    # print(actualsong)
    # print(type(actualsong))
    # print(len(actualsong))
    if len(actualsong) > 3:
        # artistname= "Artist: "+str(actualsong[2])
        # print(artistname)
        # songname= "Song:" +str(actualsong[3])
        # print(songname[:songname.find("-chord")])
        # dic["artist"]=artistname
        # dic["song"]=songname
        tempsong=actualsong[3].replace("-"," ").split("chord")
        tempsong2 = tempsong[0].split("tabs")
        # print(tempsong2)
        # ch=tr.split("chord")
        # ch1 = str(tr)
        songlist.append(str(tempsong2[0]))
        artistlist.append(str(actualsong[2]))

for x in range(len(songlist)):
    print(artistlist[x]+ " - "+ songlist[x])
    
# for songs in songlist:
#     tr = songs
#     tr2 = tr.replace("-"," ")
#     print(tr2)
#     ch= tr2.split("chord")
#     print(ch[0])



    
    
