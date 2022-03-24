# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# N = int(input('Write number N: '))
# if N == ' ':
#     print('Incorrect number')
# else:
#     temp = 1
#     lst1 = []
#     lst1.append(temp) 
#     for i in range(N - 1):
#         temp *= -3
#         lst1.append(temp)
#     print(lst1)    

# Возможно решение и с помощью функции

# N = int(input('Write number N: '))          # Вводим число N

# def get_list(N):                            # Создаем функцию получения списка из последовательности
#     return [((-3)**i) for i in range(N)]    # Возвращаем заполненный список
# print(get_list(N))                          # Вызываем функцию через print
        
# Еще одно решение но короткое
lst = []
N = int(input('Write number N: '))
n = 1
for i in range(N): 
    lst.append(n)
    n *= -3
print(lst)