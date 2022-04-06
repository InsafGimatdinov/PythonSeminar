# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найти его.

import random

def get_input_int(arg_text):
    
    '''Get integer enter users'''
    
    while True:
        
        try:
            
            input_value = input(arg_text)
            
        except:
            
            print(f'Value ({input_value}) not is integer number')
            
N = int(input('Enter quantity items sequence before sub random item: '))

original_sequence = [item for item in range(N)]

del original_sequence[random.randint(1, N - 2)]

with open('Task35_file.txt', 'w') as data:
    
    for item in original_sequence:
        
        data.write(str(f'{item} '))
        
with open('Task35_file.txt', 'r') as data:
    
    input_sequence = list(map(int, data.read().split()))
    
test_sequence = [item for item in range(input_sequence[0], len(input_sequence) + 1)]

result  = list(set(test_sequence) - set(input_sequence))

print(f'Sequence, is readline file: {input_sequence}.')  

print(f'Missing item meeting the condition A[i] - 1 = A[i - 1]: {result}')                   
    