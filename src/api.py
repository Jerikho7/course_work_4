from abc import ABC, abstractmethod
from datetime import datetime

import requests


class API(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(API):
    HH_API_URL = 'https://api.hh.ru/vacancies/'
    HH_API_URL_CITIES = 'https://api.hh.ru/suggests/areas'

    def __init__(self, keyword, city_id):
        self.params = {
            'text': keyword,
            'per_page': 1,
            'area': city_id,
            'only_with_salary': True
        }

    @classmethod
    def get_id(cls, city):
        params = {'text': city}
        response = requests.get(cls.HH_API_URL_CITIES, params=params)
        cities = response.json()
        return cities['items'][0]['id']

    def get_vacancies(self):
        data = requests.get(self.HH_API_URL, self.params).json()['items']
        # ниже полностью черновой вариант, обрабатываю какие данные взять для парсинга и что делать 'salary' (чтоб не
        # было None)
        vacancies = []
        if len(data) == 0:
            print('По вашему запросу вакансии не найдены.')
        else:
            print(f'По Вашему запросу найдено {len(data)} вакансий')
            for vacancy in data:
                published_at = datetime.strptime(vacancy['published_at'], "%Y-%m-%dT%H:%M:%S%z")
                vacancy_info = {
                    'name': vacancy['name'],
                    # 'salary_ot': vacancy['salary']['from'], #if vacancy.get('salary') else None,
                    # 'salary_do': vacancy['salary']['to'], #if vacancy.get('salary') else None,
                    'salary' : vacancy['salary'],
                    'responsibility': vacancy['snippet']['responsibility'],
                    'requirement' : vacancy['snippet']['requirement'],
                    'data': published_at.strftime("%d.%m.%Y")
                }
                vacancies.append(vacancy_info)
        return vacancies


class SuperJobAPI(API):
    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    SJ_API_TOKEN = 'v3.r.137955311.fff814138e7c8b255e8bd17bdcb834c4c92eddd1.e92d70bcfcb0d52a993a7593c53eb8246d679201'

    def __init__(self, keyword, city):
        self.params = {
            'keyword': keyword,
            'count': 1,
            'town': city,
            'no_agreement': 1
        }

    def get_vacancies(self):
        headers = {'X-Api-App-Id': self.SJ_API_TOKEN}
        data = requests.get(self.SJ_API_URL, headers=headers, params=self.params).json()['objects']
        return data
