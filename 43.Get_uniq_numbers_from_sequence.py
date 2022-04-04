# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

import random                                                       # import module random

sequence = [1, 2, 3, 5, 1, 5, 3, 10, 10, 100, 199, 15, 15, 17]      # Asked list numbers

result = list(filter(lambda x: sequence.count(x) == 1, sequence))   

print('first sequence = {}'.format(sequence))                       # Print first sequence

print('Second sequence = {}'.format(result))                        # Print result sequence