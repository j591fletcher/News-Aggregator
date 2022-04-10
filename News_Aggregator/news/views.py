import requests
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    r = requests.get('https://api.mediastack.com/v1/news?access_key=YOUR_ACCESS_KEY&categories=science,-technology')
    res = r.json()
    data = res['data']
    title = []
    desc = []
    img = []
    url = []

    #loop through data
    for i in data:
        title.append(i['title'])
        desc.append(i['description'])
        img.append(i['image'])
        url.append(i['url'])

    #display information gathered above
    news = zip(title,desc, img, url)
    
    return render(request, 'news/index.html', {'news':news})
