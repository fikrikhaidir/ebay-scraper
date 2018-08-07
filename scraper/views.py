import scrapy

def home(request):
    response = scrapy.Request('https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=apple&_sacat=0')
    response = response.css('h3.s-item__title::text').extract()
    context =   {
        'items' : response,
    }
    return render(request,'index.html',context)
