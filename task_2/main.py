""" Задание 2
Написать тест с использованием pytest и requests, в котором:
● Адрес сайта, имя пользователя и пароль хранятся в config.yaml
● conftest.py содержит фикстуру авторизации по адресу
 https://test-stand.gb.ru/gateway/login с передачей параметров 
 “username" и "password" и возвращающей токен авторизации

● Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого пользователя,
 для этого выполняется get запрос по адресу
 https://test-stand.gb.ru/api/posts c хедером,
 содержащим токен авторизации в параметре "X-Auth-Token".
 Для отображения постов другого пользователя передается "owner":
 "notMe"."""

import requests
import yaml

with open('/Users/sona/Desktop/AutoTest_Python/Seminar_1/task_2/config.yaml') as f:
    data = yaml.safe_load(f)

def login():
    response = requests.post(data['url_login'],
                         data={'username': data['login'], 'password': data['password']})
    if response.status_code == 200:
        return response.json()['token']

def get(token):
    resourсe = requests.get(data['url_posts'],
                        headers={'X-Auth-Token': token},
                        params={'owner': 'notMe'})
    return resourсe.json()

def post(token):
    new_post = requests.post(data['url_posts'],
                            data={'title': "Новый пост",
                            'description': "Мое первое автотестирование",
                            'content':"Добавить в задание с REST API еще один тест,\
                                    в котором создается новый пост,\
                                    а потом проверяется его наличие\
                                    на сервере по полю “описание"},
                            headers={'X-Auth-Token': token})
    return new_post.json()

def get_post(token):
    resourсe = requests.get(data['url_posts'],
                        headers={'X-Auth-Token': token},)
    return resourсe.json()



