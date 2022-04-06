# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10]   # Asked numbers list

uniq_numbers = list(set(numbers))     # Used standart function set

print(uniq_numbers)                   # Print result
