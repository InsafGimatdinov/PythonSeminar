# 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = int(input('Write number N: '))
if N == ' ':
    print('Incorrect number')
else:
    temp = 1
    lst1 = []
    lst1.append(temp) 
    for i in range(N - 1):
        temp *= -3
        lst1.append(temp)
    print(lst1)    
