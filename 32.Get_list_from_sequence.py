# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10]   # Asked numbers list

uniq_numbers = list(set(numbers))     # Used standart function set

print(uniq_numbers)                   # Print result

# ----------------------------------------------------------------------------------------------------

import random                                                       # import module random

sequence = [1, 2, 3, 5, 1, 5, 3, 10]                                # Asked list numbers

result = list(filter(lambda x: sequence.count(x) == 1, sequence))   

print('first sequence = {}'.format(sequence))                       # Print first sequence

print('Second sequence = {}'.format(result))                        # Print result sequence

