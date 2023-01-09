# 1.주소 잘 나오는지 확인
# 2.import request 해서 셀레니엄이 필요한 동적인지 확인
# 3.from bs4 
# 4. url 주소 입력
# 5. res = request.get(url) url 정보를 res 에 넣을려고
# 6. soup = beautifulSoup(res.text,"lxml")
# 7 soup 정보 출력 있으면 그대로 쓰고 없으면 user agent  
# 8. with open(파일명 "W" encoding= "utf8") as f:
#     f.write(soup.prettify()) #제대로 정보 받는지 확인 