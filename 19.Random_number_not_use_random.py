# 19. Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел.

from random import shuffle                                    # Import module random shuffle

import time                                                   # Import module time

def get_random_number(start, stop):                           # Create function
    
    '''Function for the interval of the                       
        
    beginning and end of time'''            
    
    sequence = [items for items in range(start, stop + 1)]    # Take time in second for assign items
    
    second = str(time.time())                                 # Translation int type time in string type
    
    index = int(second[len(second) - (len(str(stop)) - 1):])  
    
    shuffle(sequence)                                         # Mesh our first sequence
    
    return sequence[index]                                    # Return item from this sequence

print(get_random_number(-100, 100))                           # Print result item from this range

