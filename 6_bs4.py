import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# all information saved in the soup 
#print(soup.title)
#print(soup.title.get_text())

# print(soup.a) # the first a information
# print(soup.a.attrs) # the attribute of a element 
# print(soup.a["href"]) # the value of [] in a element 

#print(soup.find("a",attrs={"class":"Nbtn_upload"}))
# attrs 중에 처음으로 발견되는 a 가져오는것이다 

#print(soup.find(attrs={"class":"Nbtn_upload"}))
# 이때는 저 클래스가 중복되지 않기때문에 똑같은 결과값을 만든다

#rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2=rank1.next_sibling.next_sibling
# #왜 두번? 뛰어쓰기 때문에 
# rank3=rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2=rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# rank2= rank1.find_next_sibling("li")
# print(rank2 .a.get_text())
# rank3= rank2.find_next_sibling("li")
# print(rank3.a.get_text())

#랭크 1 부터 10 까지 다 원할때
#print(rank1.find_next_siblings("li"))

#rank1 정보 안쓰고 하는 법 
#text 는 태그 사이에 있는 글 
webtoon = soup.find("a",text="내 남편과 결혼해줘-외전 3화")
print(webtoon)