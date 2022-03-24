# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

text_first = input('Введите текст 1')
text_second = input('Введите текст 2') 

print(text_second.count(text_first))
print(text_first.count(text_second))

# # Можно было и с помощью функции

# from itertools import count               # Вызываем модуль Itertools для возвращения значения count

# text1 = str(input('Write text1: '))       # Вводим первый текст
# text2 = str(input('Write text2: '))       # Вводим второй текст

# def find_determine_count(text1, text2):      # Создаем функцию для определения пересечения двух текстов
    
#     return text2.count(text1)             # Возвращаем количество пересечений

# print('count = ', find_determine_count(text1, text2))    # Вызываем функцию 