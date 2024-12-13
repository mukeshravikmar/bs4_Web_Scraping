import pandas as pd
import requests
from bs4 import BeautifulSoup
import time


Product_name=[]
Product_url=[]
Prices =[]
Rating=[]
Num_review=[]

Pages_to_scrape=20

headers = {
    'User-Agent': '#Paste Your USER_AGENT',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',  
    'Connection': 'keep-alive'
}
for page in range(1,Pages_to_scrape+1):

    
    url = "#Use_Product_Link" + str(page) # paste the Product link 
    
 
    request= requests.get(url ,headers=headers)


    soup = BeautifulSoup(request.text,"lxml")
   
  
    container = soup.find("div", class_ = "DOjaWF gdgoEp")
    
    Products = container.find_all("div", class_ = "_75nlfW")
    
    for Product in Products :
        try :
            name = Product.find("div",class_ ="KzDlHZ").text.strip()
            
        except:
            name = " "
        Product_name.append(name)

        try:
            p_url= "#Use_Main_URL_LINK"+ Product.find("a", class_="CGtC98")['href']  #Use Main URL_link like Flipkart,Amazon etc.
            
        except:
            p_url=" "
        Product_url.append(p_url)

        try :
            price = Product.find("div", class_ = "Nx9bqj _4b5DiR").text.strip()
           
        except:
            price = " "
        Prices.append(price)

        try:
            rating = Product.find("div", class_ = "XQDdHH").text.strip()
          
        except:
            rating = "Not Available"
        Rating.append(rating)

        try:
            n_review=Product.find("span",class_="Wphh3N").text.split()[3]
            
        except:
            n_review="0"
        Num_review.append(n_review)
    

    time.sleep(2)


     
df = pd.DataFrame({"Product Name":Product_name,"Product Url":Product_url,"Prices":Prices,"Rating":Rating,"Number of Review":Num_review})
df.to_csv("Products_1.csv", index=False)