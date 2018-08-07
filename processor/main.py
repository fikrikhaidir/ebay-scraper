#!/usr/bin/env python

from lxml import html
import requests
from pprint import pprint
import unicodecsv as csv
from traceback import format_exc
import argparse

def parse(brand):
    for i in range(5):
        try:
            # url = 'http://www.ebay.com/sch/i.html?_nkw={0}&_sacat=0'.format(brand)
            url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={0}&_sacat=0'.format(brand)
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
            print ("Retrieving %s"%(url))
        	# response = requests.get(url, headers=headers, verify=False)
            response = requests.get(url)
            print (response.status_code)
            print ("Parsing page")
            parser = html.fromstring(response.text)
            product_listings = parser.xpath('//li[contains(@class,"s-item")]')
            raw_result_count = parser.xpath("//h1[@class='srp_controls__count-heading']//text()")
            result_count = ''.join(raw_result_count).strip()
            print ("Found {0} results for {1}".format(result_count,brand))
            scraped_products = []
            print (scraped_products)

            for product in product_listings:
                raw_url = product.xpath('.//a[@class="s-item__link"]/href')
                raw_title = product.xpath('.//a[@class="s-item__title"]/text()')
                raw_price = product.xpath(".//li[contains(@class,'s-item__price')]//span[@class='italic']//text()")
                price  = ' '.join(' '.join(raw_price).split())
                title = ' '.join(' '.join(raw_title).split())
                data = {
			             'url':raw_url[0],
	                     'title':title,
                         'price':price
                         }
                scraped_products.append(data)
                return scraped_products
        except Exception as e:
        	print (format_exc(e))

if __name__=="__main__":

	argparser = argparse.ArgumentParser()
	argparser.add_argument('brand',help = 'Brand Name')
	args = argparser.parse_args()
	brand = args.brand

	scraped_data =  parse(brand)
	print ("Writing scraped data to %s-ebay-scraped-data.csv"%(brand))

# 	with open('%s-ebay-scraped-data.csv'%(brand),'wb') as csvfile:
# 		fieldnames = ["title","price","url"]
# 		writer = csv.DictWriter(csvfile,fieldnames = fieldnames,quoting=csv.QUOTE_ALL)
# 		writer.writeheader()
# 		for data in scraped_data:
# 			writer.writerow(data)
