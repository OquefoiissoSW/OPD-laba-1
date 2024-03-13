from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    # proxies = {
    #     'http': 'http://proxy.omgtu:8080',
    #     'https': 'http://proxy.omgtu:8080'
    # }
    url = 'https://omgtu.ru/news/' # передаем необходимы URL адрес
    #page = requests.get(url, proxies=proxies, verify=False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    page = requests.get(url, verify=False)
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    file = open("news.txt", "w")
    block = soup.findAll('h3', class_='news-card__title') # находим контейнер с нужным классом
    description = ''
    # for data in block: # проходим циклом по содержимому контейнера
    #     if data.find('h3', class_='news-card__title'): # находим тег <p>
    #         description = data.text # записываем в переменную содержание тега
    #         file.write(description)
    count = 1
    for data in block: # проходим циклом по содержимому контейнера
        description = data.text.strip() # записываем в переменную содержание тега
        file.write(str(count) + ") " + description + "\n")
        count+=1
    file.close()
    print(description)