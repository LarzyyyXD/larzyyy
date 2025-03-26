# Задание 2. Разработка и тестирование калькулятора статистики
#  Описание: Напишите класс StatisticsCalculator, который умеет вычислять
# среднее арифметическое, медиану и дисперсию для списка чисел.
#  Что нужно сделать:
# • Реализовать методы mean(), median(), variance().
# • Написать тесты для проверки:
# o Корректности расчетов для разных входных данных.
# o Обработки пустого списка и исключений.
# o Работы с большими числами и дробными значениями.


class StatisticsCalculator:
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("error")
        self.data = data

    def mean(self):
        if not self.data:
            raise ValueError("error")
        return sum(self.data) / len(self.data)

    def median(self):
        if not self.data:
            raise ValueError("error")
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:  
            return sorted_data[mid]

    def variance(self):
        if not self.data:
            raise ValueError("error")
        mean_value = self.mean()
        return sum((x - mean_value) ** 2 for x in self.data) / (len(self.data) - 1)