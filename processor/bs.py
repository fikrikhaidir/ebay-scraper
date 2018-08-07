#!/usr/bin/env python3

import urllib2
from bs4 import BeautifulSoup

# quote_page = 'https://www.pythonforbeginners.com'
# page = urllib2.urlopen(quote_page)
# soup = BeautifulSoup(page, 'html.parser')
# name_box = soup.find('h3', attrs={'class': 's-item__title'})
# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print (name)

quote_page = 'https://www.ebay.com/itm/Apple-iPhone-6s-16GB-32GB-64GB-128GB-Unlocked-SIM-Free-Smartphone-Various-Grades/282922243372?epid=216253193&hash=item41df7ad52c%3Am%3AmggfJ2XBfcJDq_AAT_NeU4A&var=582782687415&_sacat=0&_nkw=apple&_from=R40&rt=nc&_trksid=m570.l1313'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page,'html.parser')
name_box = soup.find('h3',attrs={'class':'s-item__title'})
name = name_box.text.strip()
print (name)
#
# price_box = soup.find(‘’, attrs={‘class’:’price’})
# price = price_box.text
# print (price)
