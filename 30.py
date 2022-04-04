# 30. Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141. 10-1d10-10

import math                                                               # Import mathematics module

def New_pi(d):                                                            # Create function for find factor
    
    '''function for find new pi round values'''                           # Comment for function
    
    if 0.1  >= d > 10 ** -10:                                             # If d on this range
        
        for_round = len(str(d)) - 2                                       # Delete first sign and point from float number
        
        pi = math.pi                                                      # Used mathematics functions pi
        
        new_pi = round(pi, for_round)                                     # New_pi assigned round value
        
    else:
        
        new_pi = 'd is not in range'                                      # Else d is not in range
    
    return new_pi                                                         # Return new_pi value

d = float(input('Write accuracy factor (from 10 ** -1 to 10 ** -10): '))  # Challenge range to d

print(New_pi(d))                                                          # Print result taking into sign