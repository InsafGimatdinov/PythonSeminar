# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

N = int(input('Введите число N'))# Приглашение ко вводу числа пользователя
lst = []  # Создаем пустой лист куда в последующем внесем набор полученный
s = 1   
for i in list(range(1, N + 1)):  # Цикл for для перебора списка 
    s *= i
    lst.append(s)   # Добавляем полученный набор в lst с промощью функции append
print(lst)