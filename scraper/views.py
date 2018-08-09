from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
import requests
from bs4 import BeautifulSoup

def home(request):
    resArray = []
    res = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=dildo&_sacat=0')
    soup = BeautifulSoup(res.content)
    for title in soup.select('.s-item__title'):
        resArray.append({'name':title.text,'price':''})
    count=0
    for price in soup.select('.s-item__price'):
        try:
            resArray[count]['price'] = price.text
            count+=1
        except IndexError:
            pass
    context =   {
        'data' : resArray,
    }
    return render(request,'index.html',context)
