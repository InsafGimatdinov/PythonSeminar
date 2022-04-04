# 23. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

# import math                                     # Import mathematics module

# lst = [2, 3, 4, 5, 6]                           # Asked some list

# res_lst = []                                    # Asked some empty list

# len_res_lst = math.ceil(len(lst) / 2)           # Some Variable assigned for rounding the number up to int 

# for item, x in enumerate(lst):                  # Sort through item used cycle automatic index enumerate
    
#     if len(res_lst) != len_res_lst:             # If length res_lst not equally len_res_lst
        
#         temp = lst[item] * lst[-1 - item]       # Then temporary assigned multiply 
        
#         res_lst.append(temp)                    # Add temporary value in list
        
# print(lst)                                      # Print first list

# print(res_lst)                                  # Print result final list

# -------------------------------------------------------------------------------------------------------------------

def multi_pair(list_multi_pair):                                                   # Create function for find multiply
    
    '''Function for find multiply of pairs numbers'''                              # Function comment
    
    new_list = []                                                                  # Create new empty list
    
    if (len(list_multi_pair) % 2 == 0):                                            # If length list uneven 
        
        for item in range(0, len(list_multi_pair) // 2):                           # Then sort through item in this range
            
            new_list.append(list_multi_pair[item] * list_multi_pair[-1 - item])    # And Add multiply items in empty list
            
    else:
        
        for item in range(0, (len(list_multi_pair) + 1) // 2):                     # Else sort through item in another range
            
            new_list.append(list_multi_pair[item] * list_multi_pair[-1 - item])    # And Add multiply items in empty list
            
    return new_list                                                                # Return this new_list 

list1 = [4, 5, 2, 4, 10]                                                           # Asked first variant list

list2  = [5, 1, 4, 5, 6, 7]                                                        # Asked second variant list

print(list2)                                                                       # Print list for second variant

print(multi_pair(list2))                                                           # Print result multiply for second variant