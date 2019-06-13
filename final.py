from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://losangeles.craigslist.org/search/sss?query=honda+civic&sort=rel&min_price=1000&max_price=20000'
    #open a page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

    #parser html
page_soup = soup(page_html, "html.parser")
    #grab each item
containers = page_soup.findAll('li', {'class':'result-row'})


for record in containers:
  name = record.p.a.text
  price = record.findAll('span',{'class':'result-price'})
  pricen= price[0].text
  print('name:'+name+'      ''price:'+ pricen)

print('continute for the rest of pages')
l=120
while l<480:
  my_url='https://losangeles.craigslist.org/search/sss?max_price=20000&min_price=1000&query=honda%20civic''&s='+str(l)+'&sort=rel'
  uClient = uReq(my_url)
  page_html = uClient.read()
  uClient.close()

    #parser html
  page_soup = soup(page_html, "html.parser")
    #grab each item
  containers = page_soup.findAll('li', {'class':'result-row'})


  for record in containers:
    name = record.p.a.text
    price = record.findAll('span',{'class':'result-price'})
    pricen= price[0].text
    print('name:'+name+'      ''price:'+ pricen)
    l=l+120
else:
  print('end of all listings')