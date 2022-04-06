# Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя.

import random                                   # Import module random

list_example = [1, 5, 2, 3, 4, 6, 1, 7]         # Asked some list

n = len(list_example)                           # Assigned to variable n length list

i = 0                                           # Asked first index

list_rise = [list_example[0]]                   # Assigned to variable first index 0 from list

how_try = 0                                     

while i < n - 1:                                    
    
    how_try += 1
    
    j = random.randint(i, n - 1)                # Second index j assigned from random
    
    print(f'try: {how_try}; test_i: {j}')       
    
    if list_example[i] < list_example[j]:       # Compare two items in list
        
        list_rise.append(list_example[j])       # And add this, which more
        
        i = j                                   # First index assigned second index j

print(list_rise)                                # Print result list to console