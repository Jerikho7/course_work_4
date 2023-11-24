from abc import ABC, abstractmethod
from datetime import datetime

import requests

from src.vacancy import Vacancy


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

    def __init__(self, keyword):
        self.params = {
            'text': keyword,
            'per_page': 100,
            'only_with_salary': True
        }

    def get_vacancies(self):
        data = requests.get(self.HH_API_URL, self.params).json()['items']
        return data

    def creat_vacancy(self, data):

        if len(data) == 0:
            print('По вашему запросу вакансии не найдены.')
            Vacancy.all = {}
        else:
            print(f'По Вашему запросу на hh.ru найдено {len(data)} вакансий')
            for vacancy in data:
                published_at = datetime.strptime(vacancy['published_at'], "%Y-%m-%dT%H:%M:%S%z")
                vacancy_name = vacancy['name']
                vacancy_salary_ot = vacancy['salary']['from'] if vacancy.get('salary') else None
                vacancy_salary_do = vacancy['salary']['to'] if vacancy.get('salary') else None
                vacancy_responsibility = vacancy['snippet']['responsibility']
                vacancy_date = published_at.strftime("%d.%m.%Y")
                vacancy = Vacancy(vacancy_name, vacancy_salary_ot, vacancy_salary_do, vacancy_responsibility,
                                  vacancy_date)
                Vacancy.all


class SuperJobAPI(API):
    SJ_API_URL = 'https://api.superjob.ru/2.0/vacancies/'
    SJ_API_TOKEN = 'v3.r.137955311.fff814138e7c8b255e8bd17bdcb834c4c92eddd1.e92d70bcfcb0d52a993a7593c53eb8246d679201'

    def __init__(self, keyword):
        self.params = {
            'keyword': keyword,
            'count': 100,
            'no_agreement': 1
        }

    def get_vacancies(self):
        headers = {'X-Api-App-Id': self.SJ_API_TOKEN}
        data = requests.get(self.SJ_API_URL, headers=headers, params=self.params).json()['objects']
        return data

    def creat_vacancy(self, data):
        vacancies = []
        if len(data) == 0:
            print('По вашему запросу вакансии не найдены.')
            Vacancy.all = {}
        else:
            print(f'По Вашему запросу на superjob.ru найдено {len(data)} вакансий')
            for vacancy in data:
                date_published = datetime.fromtimestamp(vacancy.get('date_published', ''))
                vacancy_name = vacancy.get('profession', ''),
                vacancy_salary_ot = vacancy.get('payment_from', '') if vacancy.get('payment_from') else None
                vacancy_salary_do = vacancy.get('payment_to') if vacancy.get('payment_to') else None
                vacancy_responsibility = vacancy.get('candidat').replace('\n', '').replace('•', '') if vacancy.get('candidat') else None
                vacancy_date = date_published.strftime("%d.%m.%Y")
                vacancy = Vacancy(vacancy_name, vacancy_salary_ot, vacancy_salary_do, vacancy_responsibility,
                                  vacancy_date)
