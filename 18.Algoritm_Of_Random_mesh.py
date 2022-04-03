# 18. Реализовать алгоритм перемешивания списка.

# import random

# n = int(input('Write number n, please: '))

# def get_list(n, left, right):

#     return [random.randint(left, right) for item in range(n)]

# def get_mixing_list(lst):

#     return random.shuffle(lst)

# left = -20

# right = 50

# mix_list = get_list(n, left, right)

# get_mixing_list(mix_list)

# print(mix_list)

# -------------------------------------------------------------------------------------------------------------

# import random

# n = int(input('Write your number: '))

# def get_list(n):

#     lst = []

#     for item in range(-n, n + 1):

#         lst.append(item)

#     return lst

# some_list = get_list(n)

# print(some_list)

# def get_mix_list(lst):
    
#     return random.shuffle(lst)

# get_mix_list(some_list)

# print(some_list)

# ---------------------------------------------------------------------------------------------------------

from random import randrange                        # Do import module for random mesh list

n = int(input('Write your number: '))               # Asked User enter number

def get_list(n):                                    # Create function for generate new list 
    
    '''Function for create new list'''              # Commet for function
    
    first_list = []                                 # Create new empty list 
    
    for item in range(-n, n + 1):                   # Sort through item cycle
        
        first_list.append(item)                     # Add this sort items in empty list
    
    return first_list                               # Return this list

def mixed_list(items):                              # Create function for mixed item in list 
    
    '''Function for mesh list'''                    # Comment for function
    
    i = len(items)                                  # First index i assign length list items
    
    while i > 1:                                    # While this index less 1
        
        i -= 1                                      # index = index - 1
        
        j = randrange(i)                            # Second index j assign random from first index i 
        
        items[j], items[i] = items[i], items[j]     # Swap places values
        
    return items                                    # Return this items list

no_mixed_list = get_list(n)                         # Challenge function for assign new variable  

print(f'First list = {no_mixed_list}')              # Print result first list
 
print(f'Mesh list = {mixed_list(no_mixed_list)}')   # Print result mesh and finally list
    