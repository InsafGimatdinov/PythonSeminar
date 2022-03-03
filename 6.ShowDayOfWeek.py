# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

number_of_day = int(input('Введите номер дня недели: '))

r = range(0, len(week) + 1)

if (number_of_day > 0 and number_of_day < 8):
    for i in r:
        if number_of_day == i:
            print(week[number_of_day - 1])
            if (number_of_day > 5 and number_of_day < 8):
                print('День недели выходной')
            else:
                print('День недели не выходной')
else:
    print('Число вне диапазона!')

# Можно просто выписать каждый день недели отдельно но код будет длиннее