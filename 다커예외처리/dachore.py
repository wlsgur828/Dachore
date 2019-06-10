import requests

# banner
f=open("text.txt",'r')
data=f.read()
print(data)
f.close()

while(True):
    imageName = input ('plz imageName = ')
    url = 'http://13.209.35.206:8000/DachoreApp/'+imageName
    res = requests.get(url)
    if res.status_code == 404:
        continue
    else:
        print (res.text)
        break
        