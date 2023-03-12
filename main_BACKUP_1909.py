<<<<<<< HEAD
import requests
##погода сейчас
city = "Moscow,RU"
appid = "dbbc430e2e870d93116202a306988777"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра", data['wind']['speed'])
print("Видимость", data['visibility'])

##Прогноз на неделю
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <",'{0:+3.0f}'.format(i['main']['temp']),"> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nВидимость <", i['visibility'],"> \r\nСкорость ветра <", i['wind']["speed"],">")
    print("____________________________")
=======
sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]

sides = sorted(sides, reverse=True)

smax = 0
for i in range(len(sides)):
    for j in range(i + 1, len(sides)):
        for k in range(j + 1, len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
                if s > smax:
                    smax = s

print("Максимальная площадь треугольника", smax)
>>>>>>> 0f17457541bf3d403449e3a2e637fc828da830b8
