n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class std:
    def __init__(self,date,day,weather):
        self.date=date
        self.day=day
        self.weather=weather

ls=[]

for i in range(n):
    ls.append(std(date[i],day[i],weather[i]))

ls.sort(key=lambda x: x.date)

for i in range(n):
    if ls[i].weather=="Rain":
        print(ls[i].date,ls[i].day,ls[i].weather,sep=" ")
        break
    