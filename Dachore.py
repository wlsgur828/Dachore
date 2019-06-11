import requests
import os

os.system("clear")

# banner
f = open("banner.txt",'r')
data=f.read()
print(data)
f.close()

while(True):
  imageName = input ('plz imageName = ')
  url = 'http://13.209.35.206:8000/DachoreApp/'+imageName
  print ("\n        ---------- {} Analyzing ----------\n".format(imageName))
  res = requests.get(url)
  
  if res.status_code == 404:
    print ("\n"+res.text+"\n")
    continue
  elif res.status_code == 200:
    print (res.text)
    break
