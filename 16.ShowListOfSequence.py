# 16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

# n = int(input('Write number n: '))

# def create_list(n):
#     return [round((1 + 1 / x)**x, 2) for x in range(1, n + 1)]

# list = create_list(n)
# print(list)

# def find_sum(list):
#     return (round(sum(list)))

# sum = find_sum(list)
# print(sum)
# ----------------------------------------------------------------
n = int(input('Write number n: '))                        # Ввели число n для подстановки в формулу            
start = int(input('Write number start: '))                # Ввели число с которого начинается последовательность.
list = [start]                                            # Создаем список с начальным значением последовательности.
for item in range(n - 1):                                 # Вызываем цикл для создания нового списка.
    list.append(list[item] * (1 + 1 / n)**n)              # Добавляем новый набор элементов в список. 
print(list)                                               # Печатаем новый список.