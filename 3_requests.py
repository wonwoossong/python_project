import requests
res=requests.get("http://google.com")
print("request code:",res.status_code)#200 이면 정상

# if res.status_code==requests.codes.ok:
#     print("good")
# else:
#     print("there is the problem [error code]",res.status_code,"]")


#same code 
res.raise_for_status() #error raise and exit program
print("lets do the web scrapping")

print(len(res.text))

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)
#we access to the page which we want and made the file 