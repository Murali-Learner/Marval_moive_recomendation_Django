from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
# Create your views here.
load_dotenv()  # loads the .env file


def home(request):
    key = os.getenv('API_KEY')
    url = "https://api.themoviedb.org/4/list/1?page=1&api_key="+key
    response = requests.get(url).json()
    print(response)
    # print(response.backdrop_path)
    return render(request, 'home.html', {'moviedata': response["results"], 'newsData': extractcontent(), })


def extractcontent():
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

        except:
            pass
    return content_dic
