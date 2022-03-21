# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.

# x = int(input('Введите координату X'))
# y = int(input('Введите координату Y'))

# if (x > 0 and y > 0):
#     print('Точка с координатами x = ', x, 'y = ', y, 'находится в первой четверти плоскости')
# elif (x < 0 and y > 0):
#     print('Точка с координатами x = ', x, 'y = ', y, 'находится во второй четверти плоскости')
# elif (x < 0 and y < 0):
#     print('Точка с координатами x = ', x, 'y = ', y, 'находится в третьей четверти плоскости')
# elif (x > 0 and y < 0):
#     print('Точка с координатами x = ', x, 'y = ', y, 'находится в четвертой четверти плоскости')
# elif (x > 0 or x < 0) and y == 0:
#     print('Точка с координатами x = ', x, 'y = ', y, 'находится на оси X')
# elif x == 0 and (y > 0 or x < 0):
#     print('Точка с координатами x = ', x, 'y = ', y, 'находится на оси Y')
# elif (x == 0 and y == 0):
#     print('Точка с координатами x = ', x, 'y = ', y, 'находится в начале осей координат')

# Решение с помощью функции

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

def get_quarter_number(x, y):
    if x != 0 and y != 0:
        if x * y > 0:
            if x > 0:
                return 'Quarter 1'
            else:
                return 'Quarter 3'
        elif x < 0:
            return 'Quarter 2'
        else: 
            return 'Quarter 4' 
    elif x == 0:
        return 'The point is on the axis OY'
    else:
        return 'The point is on the axis OX'
    
print(get_quarter_number(x, y))
        