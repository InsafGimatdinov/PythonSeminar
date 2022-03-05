# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

text_first = input('Введите текст 1')
text_second = input('Введите текст 2') 
print(f'{text_first}', f'\n{text_second}')

count = text_first.count(text_second)

print('count = ', count)