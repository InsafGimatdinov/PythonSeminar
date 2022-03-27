# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# import random                                                                # Импортировали модуль random

# N = int(input('Write number N: '))                                           # Ввели число N

# def func(N):                                                                 # Создали функцию для получения списка
#     '''Создание списка из N элементов'''                                     # В таких тройных кавычках внутри функции 
#                                                                              # делаем комментарий. 
#     lst = []                                                                 # Создали пустой список
#     for item in range(-N, N, 2):                                             # Перебираем элементы с шагом 2
#         lst.append(item)                                                     # Добавляем элементы в пустой созданный список
#     return lst                                                               # Возвращаем этот список

# spisok = func(N)                                                             # Вызываем функцию для переменной spisok
# print(spisok)                                                                # Выводим на печать список
# pozitions = [random.randrange(N) for item in range(random.randrange(N))]     # Позиции которые должны перемножаться

# with open('file_Task17.txt', 'w') as data:                                   # Открываем файл для записи в него данных
#     for item in range(0, len(pozitions)):                                    # Перебираем элементы для заполнения позиций
#         data.write(f'{pozitions[item]}\n')                                   

# product = 1                                                                  # Переменная mult произведение
# path ='file_Task17.txt'                                                      # Переменной path передаем файл .txt
# data = open(path, 'r')                                                       # Открываем файл для чтения
# for line in  data:                                                           # Перебираем строки в этом файле
#     print(line)                                                              # Печатаем значения в этих строках
#     product *= spisok[int(line)]                                                
# data.close()                                                                 # Разрываем соединение с этим файлом           
# print(product)                                                               # Печатаем конечный результат
# ---------------------------------------------------------------------------------------------------------------------------------
# from random import randint
# with open('file_Task17.txt', 'w') as data:
#     data.write('1\n')
#     data.write('5\n')
#     data.write('2\n')
#     data.write('2\n')
#     data.write('1\n')
#     data.write('0\n')
    
# def get_numbers(N):
#     return [randint(-N / 2, N) for item in range(-N, N + 1)]

# def get_data_from_file(path):
#     data = open(path, 'r')
#     d_list = [int(line.strip()) for line in data]
#     data.close()
#     return d_list

# def get_product(numbers, datalist):
#     product = 1
#     for item in datalist:
#         product *= numbers[item]
#     return product

# path = 'file_Task17.txt'
# N = int(input('Write number N: '))
# data_list = get_data_from_file(path)
# numbers = get_numbers(N)

# print(numbers)
# print(data_list)
# print(get_product(numbers, data_list))
# --------------------------------------------------------------------