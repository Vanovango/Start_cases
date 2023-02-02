import os
import subprocess
import sys
import webbrowser

import voice

try:
    import requests
except:
    pass


def weather():
    try:
        params = {'q': 'Saint Petersburg', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def browser():
    webbrowser.open('https://www.youtube.com', new=2)


def game():
    try:
        subprocess.Popen('C:\Program Files (x86)\Steam\Steam.exe')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    voice.speaker('До новых встреч')
    os.system("shutdown -s")
    sys.exit()

def offBot():
    sys.exit()


def passive():
    pass
