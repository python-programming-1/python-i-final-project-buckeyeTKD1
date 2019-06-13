from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
kbb_price=6000             #it's impossible to scrap kbb, so you need to check it manually
city='losangeles'          #enter the name of your city, no space
make='ford'              #enter the make of the vehicle
model='F150'               #enter the model of the vehicle
min_price='2000'                  #|          |
max_price='50000'                 #|          |
min_year='1990'              #every thing is same here, manually change it before running it
max_year='2019'
my_url='https://'+city+'.craigslist.org/search/sss?auto_make_model='+make+'%20'+model+'&max_auto_year='+max_year+'&max_price='+max_price+'&min_auto_year='+min_year+'&min_price='+min_price+'&query='+make+'%20'+model+'&sort=rel'
    
    #open a page 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll('li', {'class':'result-row'})


for record in containers:
  name = record.p.a.text
  price = record.findAll('span',{'class':'result-price'})
  pricen= price[0].text
  
  if int(pricen.replace('$',''))>kbb_price:
    print('name:'+name+'      ''price:'+ pricen+':(')
  else:
    print('name:'+name+'      ''price:'+ pricen+':)')

print('continute for the rest of pages')
input("y/n")
l=120
total=page_soup.findAll('span', {'class':'totalcount'})
total_number_text=total[0].text
total_number_value=int(total_number_text)
while l<total_number_value:
  if l<1080:
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    my_url='https://'+city+'.craigslist.org/search/sss?s='+str(l)+'&auto_make_model='+make+'%20'+model+'&max_auto_year='+max_year+'&max_price='+max_price+'&min_auto_year='+min_year+'&min_price='+min_price+'&query='+make+'%20'+model+'&sort=rel'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    l=l+120
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll('li', {'class':'result-row'})
    for record in containers:
      name = record.p.a.text
      price = record.findAll('span',{'class':'result-price'})
      pricen= price[0].text
  
      if int(pricen.replace('$',''))>kbb_price:
        print('name:'+name+'      ''price:'+ pricen+':(')
      else:
        print('name:'+name+'      ''price:'+ pricen+':)')
    
  elif l>1050:
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    my_url='https://'+city+'.craigslist.org/search/sss?s='+str(l)+'&auto_make_model='+make+'%20'+model+'&max_auto_year='+max_year+'&max_price='+max_price+'&min_auto_year='+min_year+'&min_price='+min_price+'&query='+make+'%20'+model+'&sort=rel'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    l=l+120
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll('li', {'class':'result-row'})
    for record in containers:
      name = record.p.a.text
      price = record.findAll('span',{'class':'result-price'})
      pricen= price[0].text
  
      if int(pricen.replace('$',''))>kbb_price:
        print('name:'+name+'      ''price:'+ pricen+':(')
      else:
        print('name:'+name+'      ''price:'+ pricen+':)')
else:
    print('end of all listings')