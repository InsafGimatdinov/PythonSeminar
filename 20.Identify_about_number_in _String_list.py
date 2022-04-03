# 20. Определить, присутствует ли в заданном списке строк, некоторое число.

# new_list = ['2', 'insaf', 'moscow', '313', 'digit', 'number']     # Create new random string list

# for item in new_list:                                             # Sort through item in our string list

#     if item.isdigit():                                            # If item constitute int digit

#         print(item)                                               # Print result numbers which constitute int number
        
# ------------------------------------------------------------------------------------------------------------

# new_list = ['2', 'insaf', 'moscow', '313', 'digit', 'number']     # Create new random string list

# find_number = input('Write your number: ')                        # Create variable for user enter number

# flag = True                                                       # Add flag True

# for item in new_list:                                             # Sort through item in our string list 
    
#     if flag == False:                                             # If flag equally False
        
#         break                                                     # Do break cycle
    
#     elif item == find_number:                                     # Else if item equally in user number
        
#         print(f'First number {find_number} present in the list')  # Print result 
        
#         flag = False                                              # Flag assign False
        
# if flag == True:                                                  # If flag equally True
    
#     print(f'First number {find_number} not present in the list')  # Print message about error and try again
    
# -------------------------------------------------------------------------------------------------------------

def is_int(str):                                                        # Function for checking convert string in int type
    
    '''Function for checking int type'''                       
    
    try:                                                            
        int(str)                                                        # Convert string to int type
        
        return True                                                     # Return True
    
    except:
        
        return False                                                    # else return False
    
def find_int(str_list, some_int):                                       # Function for search int number in string list
    
    '''Function for search int type number in string list'''
    
    result = False                                                      # Variable result assigned False
    
    for item in range(0, len(str_list)):                                # Sort through item in this range
        
        if string_list[item] == str(some_int):                          # If item in string list equally string some_int
            
            result == True                                              # Result equally True
            
    return result                                                       # Return this result

string_list = input('Write random string text: ').split(' ')            # Ask user write random string list through split

some_number= input('Write rnadom int number for search in list')        # Ask user write random int type number 

while is_int(some_number) == False:                                     # While some_number equally False 
    
    some_number = input('Incorrect Enter, try again: ')                 # comes out error and try again
    
else:                                     
    
    some_number = int(some_number)                                      # Else convert some_number to int type
    
if find_int(string_list, some_number) == True:                          # If find need number equally True    
    
    print(f'Number {some_number} present in the list: {string_list}')   # Then print message about present in the list
    
else:
    
    print(f'Number {some_number} not present in the list: {string_list}') # Else print message about not present in  the list 