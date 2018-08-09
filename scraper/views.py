from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
from .forms import *

def scrape(urlTarget):
    resArray = []
    res = requests.get(urlTarget)
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
    return resArray

def home(request):
    resArray=[]
    form = ItemForm(request.POST)
    if form.is_valid():
        form_title = form.cleaned_data['title']
        form_price = form.cleaned_data['price']

    if 'search' in request.GET and request.GET['search']:
        search = request.GET['search']
        search = quote(str(search))
        res = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={0}&_sacat=0'.format(search)
        resArray = scrape(res)
        context =   {
            'data' : resArray,
        }
        return render(request,'index.html',context)
    context =   {
        'data' : resArray,
    }
    return render(request,'index.html',context)

def cart(request):
    pass
