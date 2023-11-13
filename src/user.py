from src.api import HeadHunterAPI, SuperJobAPI


def user_parsing():
    print('Поиск вакансий на сайтах hh.ru и superjob.ru.')
    website = int(input("Выберите платформы, с которых хотите получить вакансии:\n1 - hh.ru\n2 - superjob.ru\n3 - "
                        "поиск на обоих сайтах\n"))

    city = input("Выберете город для поиска либо нажмите Enter для просмотра во всех городах: ")
    if city == '':
        pass
    elif website == '1':
        try:
            city_id = HeadHunterAPI.get_id(city)
        except KeyError:
            print('Не верно введено наименование')
    elif website == '2':
        pass
    else:
        pass

    keyword = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()

    if website == '1':
        hh_api = HeadHunterAPI(keyword, city_id)
    elif website == '2':
        sj_api = SuperJobAPI(keyword, city)
    else:
        pass

    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
