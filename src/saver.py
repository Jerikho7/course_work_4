from abc import ABC, abstractmethod
import json


class Saver(ABC):
    @abstractmethod
    def write_file(self, file_name):
        pass

    @abstractmethod
    def del_info(self):
        pass

class JsonSaver(Saver):

    def __init__(self, vacancies):
        self.vacancies = vacancies

    def write_file(self, file_name):

        self.file_name = file_name
        try:
            with open(self.file_name, 'at') as f:
                json.dump(self.vacancies, f, indent=2)
        except FileNotFoundError:
            print('Ошибка в имени файла!')

    def del_info(self):

        with open(self.file_name, 'wt') as f:
            pass
