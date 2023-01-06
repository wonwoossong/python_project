
from selenium import webdriver
import time

options= webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
browser= webdriver.Chrome(options=options)
browser.maximize_window()

url="https://play.google.com/store/movies?hl=ko&gl=US"
browser.get(url)


interval=2
#현재 문서 높이 저장
prev_height=browser.execute_script("return document.body.scrollHeight")

while(True):
    #스크롤 가장 아래로
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #페이지 로딩 대기
    time.sleep(interval)
    #현재 문서 높이 저장
    curr_height=browser.execute_script("return document.body.scrollHeight")

    if curr_height==prev_height:
        break
    prev_height=curr_height
print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")



import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


soup=BeautifulSoup(browser.page_source,"lxml")

# movies = soup.find_all("div",attrs={"class":"ULeU3b neq64b"})
movies = soup.find_all("div",attrs={"class":"ULeU3b neq64b"})
print(len(movies))
 
# with open("movie.html","w",encoding="utf8") as f:
#     #f.write(res.text)
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div",attrs={"class":"Epkrse"})
    if title:
        title=title.get_text()
    else:
        continue

    #할인 전 가격 
    original_price=movie.find("span",attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price=original_price.get_text()
    else:
        #print(title,"할인 되지 않은 영화 제외")
        continue
    #할인 된 가격 
    price= movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

    #링크정보 
    link=movie.find("a",attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    
    print(f"title:{title}")
    print(f"before discount:{original_price}")
    print(f"after discoint:{price}")
    print(f"link : ","https://play.google.com"+link)
    print('-'*120)
browser.quit()


# url= "https://play.google.com/store/movies?hl=ko&gl=US"
