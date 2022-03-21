# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# x = y = z = True

# Check1 = not(x and y and z)

# Check2 = (not x) or (not y) or (not z)

# if Check1 == Check2:
#     print(True)
# else:
#     print(False)
    
# Другой вариант решения через цикл for

# x = False
# y = True
# z = False
# print(f'Исходныеданные: x = {x}, y = {y}, z = {z}')

# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):  
#             r1 = not (x or y or z)
#             r2 = not (x)and not (y) and not (z)
# if r1 == r2:
#     print('True')
# else:
#     print('False')    

# Еще один способ решения задачи через функцию

import random
import math

def is_true(x, y, z):
    check1 = not(x or y or z)
    check2 = not x and not y and not z
    return check1 == check2
signal = True
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not is_true(x, y, z):
                signal = False
            print(f'{x = }, {y = }, {z = }, result = {is_true(x, y, z)}')
if signal == True:
    print('all right')
else:
    print('not all right')