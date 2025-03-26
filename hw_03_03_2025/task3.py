# Задание 3. Разработка и тестирование файлового менеджера
# Описание: Реализуйте класс FileManager, который выполняет базовые операции с
# файлами: чтение, запись и удаление.
# Что нужно сделать:
# • Реализовать методы write_file(), read_file(), delete_file().
# • Написать тесты для проверки:
# o Корректности чтения и записи данных.
# o Обработки несуществующих файлов.
# o Работы с разными типами данных (текст, JSON, CSV).

import os
import json
import csv

class FileManager:
    def write_file(self, filename, data):
        if filename.endswith('.json'):
            with open(filename, 'w') as json_file:
                json.dump(data, json_file)
        elif filename.endswith('.csv'):
            with open(filename, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                if isinstance(data, list):
                    writer.writerows(data)
                else:
                    writer.writerow(data)
        else:   
            with open(filename, 'w') as text_file:
                text_file.write(data)

    def read_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError("файл не найден")
        
        if filename.endswith('.json'):
            with open(filename, 'r') as json_file:
                return json.load(json_file)
        elif filename.endswith('.csv'):
            with open(filename, 'r') as csv_file:
                reader = csv.reader(csv_file)
                return list(reader)
        else:
            with open(filename, 'r') as text_file:
                return text_file.read()

    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            raise FileNotFoundError("файл не найден")