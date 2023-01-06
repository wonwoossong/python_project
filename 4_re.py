#정규식: 정해진 형태의 식 

import re

p=re.compile("ca.e") 
# . (ca.e): means one character > care,cafe,case|caffffe X 
# ^ (^de): start the string  > desk,destination,devil | indeed X 
# $ (se$) : end of the string > case, base,| sequence X


m=p.match("case")
print(m)
#print(m.group()) #if that is matched print if not no print  
#m=p.match("cassssse")
#print(m.group())

def print_match(m):
    if m:
        print("m.group:",m.group())#일치하는 문자열 반환
        print("m.string:",m.string)#입력받은 문자열 출력
        print("m.start:",m.start())#일치하는 문자열의 시작 index
        print("m.end:",m.end()) # 일치하는 문자열의 끝 index
        print("m.span:",m.span()) #일치하는 문자열의 시작 끝 index 
    else:
        print("does not match")

m=p.match("careless") # it match why? it is going to check from the begining so it matched  
print_match(m)

m = p.search("good care") # it is going to check is there any matched string 
print_match(m)

lst=p.findall("good care cafe") # findall everthing which is matched change to list
print(lst)


#1. p=re.compile("원하는 형태")
#2. m = p.match("비교할 문자열") 처음부터 확인하면서 가는거
#3. m = p.search("비교할 문자열") 주어진 문자열에서 맞는게 있는지 확인
#4. m = p.findall("비교할 문자열") 일치하는 모든것을 " 리 스 트 " 형태로 반환 

# 원하는 형태 : 정규식
# . (ca.e): means one character > care,cafe,case|caffffe X 
# ^ (^de): start the string  > desk,destination,devil | indeed X 
# $ (se$) : end of the string > case, base,| sequence X
