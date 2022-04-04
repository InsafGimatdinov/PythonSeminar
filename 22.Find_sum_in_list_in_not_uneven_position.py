# 22. Найти сумму чисел списка стоящих на нечетной позиции

from random import randint                                           # From module random do import randint

# n = int(input('Write your random number n: '))                     # Maybe ask user write number n

n = 10                                                               # Maybe ask number directly

def create_new_list(n):                                              # Create function for create new random list
    
    '''Function for generate new random list'''                      # Function comment
    
    lst = []                                                         # Add empty list
    
    for item in range(n):                                            # Sort all item in this range
        
        item = randint(1, 100)                                       # Generate random number to fill list
        
        lst.append(item)                                             # Add this item in our list
    
    return lst                                                       # And return this list

new_list = create_new_list(n)                                        # Challenge function to variable

print(new_list)                                                      # Print result fill list

def find_sum_in_uneven_positions(lst):                               # Create new function for find sum items
    
    '''function for find result sum numbers in even positions'''     # Function comment
    
    sum = 0                                                          # Create some variable sum
    
    for item in range(0, len(lst)):                                  # Sort through item in this range
        
        if item % 2 != 0:                                            # if positions is uneven not equally 0
            
            sum += lst[item]                                         # Then sum + item in list

    return sum                                                       # Return this sum 

sum_of_even = find_sum_in_uneven_positions(new_list)                 # Challenge this new function to variable

print('sum = {}'.format(sum_of_even))                                # Print result in the form of sum



