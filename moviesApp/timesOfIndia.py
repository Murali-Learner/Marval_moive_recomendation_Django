from bs4 import BeautifulSoup
import requests


# def extractcontent():
toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')
body = toi_soup.find("body")
container = body.find("div", {"id": "container"})
content = (container.find("div", {"id": "content"})).find("div", {
    "class": "wrapper clearfix politics"}).find("div", {"class": "briefs_outer clearfix"})
content_list = content.find_all("div", {"class": "brief_box"})

head_list = []
content_dic = {}
for data in content_list:
    try:
        head_list.append(data.find("h2").text)
        content_list.append(data.find("p").text)
        content_dic[data.find("h2").text] = data.find("p").text
        print(content_dic)

    except:
        pass
