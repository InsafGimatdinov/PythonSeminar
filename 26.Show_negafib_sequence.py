# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# Негафибоначчи

def negfib(n):                                                      # Create function for negfib sequence
    
    '''function for negfib sequence'''                               # Function comment
    
    if n in [-1, 0, 1]:                                              # If n in this range
    
        return abs(n)                                                # Return absolute value n 
    
    elif n < 0:                                                      # If n less 0
        
        n = abs(n)                                                   # Then n assigned absoluter value n
        
        return (-1) ** (n + 1) * (negfib(n - 1) + negfib(n - 2))   # Return sequence with formula
    
    else:
        
        return negfib(n - 1) + negfib(n - 2)                       # Else return with formula
    
n = int(input('Write number n: '))                                   # Asked user write number n

list = []                                                            # Create new empty list

for item in range(-n, n + 1):                                        # Sort through items in this range
    
    list.append(negfib(item))                                       # Add function with item in empty list
    
print(list)                                                          # Print this negfib list