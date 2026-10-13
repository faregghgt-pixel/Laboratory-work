# Решение задания 7

def load_data():
    return [3, 17, 8, 25, 6, 12, 25, 9, 14]

def filter_above(values, theshold=10):
    '''возвращает список значений больше theshold'''
    big_theshold = []
    for number in numbers:
        if number>theshold:
            big_theshold.append(number)
    return big_theshold

def mean(values):
    """Среднее арифметическое."""
    return sum(values) / len(values)
