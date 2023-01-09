# 1. 네이버 에서 서울의 날씨 정보 가져온다
    # 1-1) 흐림 어제보다 ~ 높아요
    # 1-2) 현재 ~~ (최저 00 최고 00)
    # 1-3) 오전 강수 확률 00% / 오후 강수 확률 00%
# 2. 헤드 라인 뉴스 3 건을 가져온다
# 3. IT 뉴스 3건을 가져온다
# 4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup= BeautifulSoup(res.text,"lxml")
    return soup


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 1-1) 흐림 어제보다 ~ 높아요
    cast= soup.find("p",attrs={"class":"summary"}).get_text()
    #1-2) 현재 ~~ (최저 00 최고 00)
    curr_temp=soup.find("div",attrs={"class":"temperature_text"}).get_text().strip()
    min_temp=soup.find("span",attrs={"class":"lowest"}).get_text().strip()
    max_temp=soup.find("span",attrs={"class":"highest"}).get_text().strip()
    # 1-3) 오전 강수 확률 00% / 오후 강수 확률 00%
    morning_rain= soup.find("div",attrs={"class":"cell_weather"}).get_text().split()
    #print(morning_rain[1])#오전 확률
    #print(morning_rain[4])#오후 확률
    print(cast)
    print("{0} ({1} /{2})".format(curr_temp,min_temp,max_temp))
    print("오전 강수확률 {0} / 오후 강수확률 {1}".format(morning_rain[1],morning_rain[4]))

def scrape_headline_news():
    print("헤드라인 뉴스")
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
    soup = create_soup(url)
    news_list= soup.find("div",attrs={"class":"cluster_body"}).find_all("li")
    for index,news in enumerate(news_list):
        title= news.div.a.get_text().strip()
        link= url+news.find("a")
        print("{}. {}".format(index+1,title))
        print("  (link: {})".format(link))
    print()
if __name__ == "__main__":
    #scrape_weather()#오늘의 날씨 정보 가져오기
    scrape_headline_news()   