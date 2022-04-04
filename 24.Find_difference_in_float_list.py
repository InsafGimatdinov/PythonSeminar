# 24. В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math                                                                       # import mathematics module
                                                                                  
number_list = [1.1, 1.3, 3.1, 5, 10.01]                                           # Asked some float numbers list

def get_decimal_part(float_number, int_digit_after_point):                        # Create some function for get decimal parts number
    
    '''Function for get decimal number'''                                         # Function comment
    
    return round((float_number % 1), int_digit_after_point)                       # Return rounding value after point 

decimal_part_list = []                                                            # Create empty list 

for item in range(0, len(number_list)):                                           # Sort through item in this range
    
    if type(number_list[item]) == float:                                          # If type item equally float
        
        decimal_part_list.append(get_decimal_part(number_list[item], 2))          # Then add this item in list
        
max = max(decimal_part_list)                                                      # Variable max used function max

min = min(decimal_part_list)                                                      # Variable min used function min

print(f'Difference between maximum and minimum value float parts item in list: \
{number_list} => {max - min}')                                                    # Print result difference
