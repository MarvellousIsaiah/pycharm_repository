import requests

# url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m""
# r = request.get(url)
# print(r.test)
# data = r.json()


url1 = "https://th.bing.com/th/id/R.86a8179b2fabd7783eeb7c5cbe5cfa03?rik=c4aPFE24miQgvQ&pid=ImgRaw&r=0"
r2 = requests.get(url1)
print(r2.text)

with open('marvy.png', mode='wb') as mf:
    mf.write(r2.content)
