# 27. Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

def is_int(str):                                             # Create function for checking convert to integer
    
    '''function for checking convert string to integer'''    # Function comment
    
    try:
        
        int(str)                                             # If convert to integer successfull
        
        return True                                          # Then return True
    
    except:
        
        return False                                         # Else return False
    
def string_int(some_str):                                    # Create function for convert string to integer
    
    '''function for convert string to integer'''             # Function comment
    
    return [int(x) for x in some_str.split(' ')]             # Sort through elements with search integer type number

some_string = '11 5 2 -1 0 85 23 1 90 -19'                   # Asked some string list numbers

# while is_int(some_string) == False:
    
#     string_list = ('This string not have numbers!')
    
# else:
    
#     string_list = string_int(some_string)
    
string_list = string_int(some_string)                        # Challenge function in variable string_list

print(type(string_list))                                     # Print type items in list

min = min(string_list)                                       # Used function min 

max = max(string_list)                                       # Used function max

print(string_list)                                           # Print first string list

print('min = {}, max = {}'.format(min, max))                 # Print result max and min