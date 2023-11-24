class Vacancy:
    all = []

    def __init__(self, name, salary_ot, salary_do, responsibility, date):
        self.name = name
        self.salary_ot = salary_ot
        self.salary_do = salary_do
        self.responsibility = responsibility
        self.date = date
        self.all.append(self)

    def __str__(self):
        return f'Вакансия {self.name}'

    def __sub__(self, other):
        if isinstance(other, Vacancy):
            return float(self.salary_ot) - float(other.salary_ot)
        else:
            raise Exception('Нельзя вычитать данные элементы')

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return float(self.salary_ot) >= float(other.salary_ot)
        elif isinstance(other, float):
            return float(self.salary_ot) >= other
        else:
            raise ValueError('Несравниваемые объекты')

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return int(self.salary_ot) <= float(other.salary_ot)
        elif isinstance(other, float):
            return float(self.salary_ot) <= other
        else:
            raise ValueError('Несравниваемые объекты')

    def __int__(self):
        self.salary_do = None if not self.salary_do else self.salary_do
        self.salary_ot = None if not self.salary_ot else self.salary_ot
        if self.salary_ot is not None and self.salary_do is not None:
            return int((self.salary_ot + self.salary_do) / 2)
        elif self.salary_ot is not None and self.salary_do is None:
            return int(self.salary_ot)
        elif self.salary_ot is None and self.salary_do is not None:
            return int(self.salary_do)
        else:
            return 0

    @classmethod
    def get_max(cls):

        all_salaries = {}

        for vacancy in cls.all:
            if vacancy['salary_ot'] is not None:
                all_salaries[vacancy.name] = int(vacancy['salary_ot'])
            else:
                all_salaries[vacancy.name] = int(vacancy['salary_ot'])

        max_salary = max(all_salaries.values())
        max_list = list(k for k, v in all_salaries.items() if v == max_salary)
        print(f'Вакансии с максимальной зарплатой {max_salary} рублей: номер {max_list}')
        print('Информация по данным вакансиям:')
        for m in max_list:
            cls.all[m].print_info()

    def print_info(self, number_list):
        print(f'{number_list} - опубликовано {self.date} {self.name}:')

        if self.responsibility is None:
            print('Обязанности: не указано')
        else:
            print(f'Обязанности: {self.responsibility}')

        if self.salary_ot is None:
            print(f'Зарплата: {self.salary_do} рублей\n')
        elif self.salary_do is None:
            print(f'Зарплата: до {self.salary_ot} рублей\n')
        else:
            print(f'Зарплата: от {self.salary_ot} до {self.salary_do} рублей\n')

    @classmethod
    def print_info_all(cls, lenght_list):
        print(f'Вакансии:\n')
        n = 0
        for vac in cls.all[:lenght_list]:
            n += 1
            vac.print_info(n)
