# 29. Найти НОК двух чисел.

number1 = int(input('Write your number1: '))                # Asked user write number 1

number2 = int(input('Write your number2: '))                # Asked user write number 2

def nod(x1, x2):                                            # Create function
    
    '''Function for search greatest common divisor'''       # Comment for function 
    
    if x2 == 0:                                             # If x2 equally 0
        
        return x1                                           # Then return x1
    
    else:
        
        return nod(x2, x1 % x2)                             # Else return greatest common divisor  
    
print(nod(number1, number2))                                # Print this value to console

def nok(x1, x2):                                            # Create new function
    
    '''function for search the smallest common multiple'''  # Comment for function
    
    return x1 * x2 // nod(x1, x2)                           # Return this value 

print(nok(number1, number2))                                # Print result to console