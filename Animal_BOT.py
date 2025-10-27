import requests
import time
import random

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = ''

# API-шки для зверушек
CAT_API = 'https://api.thecatapi.com/v1/images/search'
DOG_API = 'https://random.dog/woof.json'
FOX_API = 'https://randomfox.ca/floof/'

# Сообщение на случай ошибки
ERROR_TEXT = 'Здесь должна была быть картинка с животным, но что-то пошло не так :('

offset = -2
counter = 0

def get_cat():
    response = requests.get(CAT_API)
    if response.status_code == 200:
        return response.json()[0]['url']
    return None

def get_dog():
    response = requests.get(DOG_API)
    if response.status_code == 200:
        url = response.json()['url']
        # Иногда dog API возвращает видео — мы их игнорируем
        if url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return url
    return None

def get_fox():
    response = requests.get(FOX_API)
    if response.status_code == 200:
        return response.json()['image']
    return None

def get_random_animal():
    fetchers = [get_cat, get_dog, get_fox]
    random.shuffle(fetchers)
    for fetch in fetchers:
        link = fetch()
        if link:
            return link
    return None

while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            photo_url = get_random_animal()

            if photo_url:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={photo_url}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
