# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

print('Введите число')
number = int(input())

if (number % 5 == 0 and number % 10 == 0):
    print('Число кратно 5 и 10')
elif (number % 15 == 0 and number % 30 != 0):   
    print('Число кратно 15 и не кратно 30')
else:
    print('Число не кратно 5, 10 и 15')