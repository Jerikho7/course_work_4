# закоментированный вариант как будет
# from src.user import user_parsing
#
# if __name__ == '__main__':
#     user_parsing()

# это вариант для отработки потом будет удален
from src.api import HeadHunterAPI

hh = HeadHunterAPI('Python', '2')

data = hh.get_vacancies()
print(data)

