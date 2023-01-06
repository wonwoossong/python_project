import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

for i in range(1,6):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    res = requests.get(url,headers=headers)

    res.raise_for_status()
    soup=BeautifulSoup(res.text,"lxml")


    items = soup.find_all("li",atrs={"class":re.compile("^search-product")})
    #print(items[0].find("div",attrs={"class":"name"}).get_text())

    for item  in items:
        #광고 제품 제외
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("no ad product")
            continue
        name = items[0].find("div",attrs={"class":"name"}).get_text()
        #apple mac no ! 
        if "Apple" in name:
            print(" <Apple 상품 제외합니다>")
            continue
        
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        
        # 리뷰 백개 이상 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate=rate.get_text()
        else:
            print("no rating ")
            continue
    
    
        rate_num = item.find("span", attrs={"class":"rating-total-count"})
        if rate_num:
            rate_num = rate_num.get_text() # (26) 인트로 바꿔야됨
            rate_num = rate_num[1:-1] #from 1 and last -1
        else:
            print("no rating")
            continue

        if float(rate)>=4.5 and int(rate_num)>=50:
            print(name,price,rate,rate_num)

        print (name,price,rate,rate_num)