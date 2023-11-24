from src.vacancy import Vacancy
from src.api import HeadHunterAPI, SuperJobAPI
from src.saver import JsonSaver


def user_parsing():
    print('Поиск вакансий на сайтах hh.ru и superjob.ru.')
    website = int(input("Выберите платформы, с которых хотите получить вакансии:\n1 - hh.ru\n2 - superjob.ru\n3 - "
                        "поиск на обоих сайтах\n"))
    keyword = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()

    if website == 1:
        hh_api = HeadHunterAPI(keyword)
        hh_data = hh_api.get_vacancies()
        hh_api.creat_vacancy(hh_data)
        user_answer = input('Сортировать список вакансий по зарплате от большей к меньшей? yes/no ')
        if user_answer == 'yes':
            veiw_number = int(input('Сколько вакансий вывести из полученного списка: '))
            list_vac = sorted(Vacancy.all, key=lambda x: -int(x))
            for item in list_vac[:veiw_number]:
                print(f"{item.name} {int(item)}\n")
        elif user_answer == 'no':
            user_answer = input('Вывести вакансию с максимальной ЗП? yes/no ')
            if user_answer == 'yes':
                Vacancy.get_max()
            if user_answer == 'no':
                veiw_number = int(input('Сколько вакансий вывести из полученного списка: '))
                Vacancy.print_info_all(veiw_number)
            else:
                print('Полный список вакансий будет сохранен в файл, посмотрите, когда будет настроение')
                file_name = input('А пока введите имя файла в формате "xxx.txt: ')
                js_saver = JsonSaver(hh_data)
                js_saver.write_file(file_name)
                print(f'Вакансии записаны в файл {file_name}\n')
                print('Всего доброго!')
                exit()
    elif website == 2:
        sj_api = SuperJobAPI(keyword)
        sj_data = sj_api.get_vacancies()
        sj_api.creat_vacancy(sj_data)
        user_answer = input('Сортировать список вакансий по зарплате от большей к меньшей? yes/no ')
        if user_answer == 'yes':
            veiw_number = int(input('Сколько вакансий вывести из полученного списка: '))
            list_vac = sorted(Vacancy.all, key=lambda x: -int(x))
            for item in list_vac[:veiw_number]:
                print(f"{item.name} {int(item)}\n")
        elif user_answer == 'no':
            user_answer = input('Вывести вакансию с максимальной ЗП? yes/no ')
            if user_answer == 'yes':
                Vacancy.get_max()
            if user_answer == 'no':
                veiw_number = int(input('Сколько вакансий вывести из полученного списка: '))
                Vacancy.print_info_all(veiw_number)
            else:
                print('Полный список вакансий будет сохранен в файл, посмотрите, когда будет настроение')
                file_name = input('А пока введите имя файла в формате "xxx.txt: ')
                js_saver = JsonSaver(sj_data)
                js_saver.write_file(file_name)
                print(f'Вакансии записаны в файл {file_name}\n')
                print('Всего доброго!')
                exit()
    elif website == 3:
        hh_api = HeadHunterAPI(keyword)
        sj_api = SuperJobAPI(keyword)
        hh_data = hh_api.get_vacancies()
        sj_data = sj_api.get_vacancies()
        hh_api.creat_vacancy(hh_data)
        sj_api.creat_vacancy(sj_data)

        veiw_number = int(input('Сколько вакансий вывести из полученного списка: '))
        Vacancy.print_info_all(veiw_number)
    else:
        print('Всего доброго!')
        exit()
