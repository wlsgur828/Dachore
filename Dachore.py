import requests
import os

# banner
f=open("banner.txt",'r')
data=f.read()
print(data)
f.close()

imageName = input ('plz imageName = ')
url = 'http://13.209.35.206:8000/DachoreApp/'+imageName
res = requests.get(url)
print (res.text)
