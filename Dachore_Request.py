import requests

print (" 도커 이미지 취약점 스캔 프로그램 Dachore ")
imageName = input ('plz imageName = ')
url = 'http://13.209.35.206:8000/DachoreApp/'+imageName
res = requests.get(url)
print (res.text)
