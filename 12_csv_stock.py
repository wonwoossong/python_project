#네이버 접속해서 코스피 시가 총액

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-200.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer=csv.writer(f)

title="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") # 이러면 스트링 형태의 리스트로 들어간다

writer.writerow(title)

for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")   
 
    data_rows=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <=1: # 의미없는 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns] #strip 함수 불 필요한 공배 지우기 
        #print(data)
        writer.writerow(data)