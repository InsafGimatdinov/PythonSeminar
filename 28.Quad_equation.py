# 28. Найти корни квадратного уравнения Ax² + Bx + C = 0
# - Математикой
# - Используя дополнительные библиотеки*

import math                                                 # Import mathematics module

from modulefinder import Module                             # import nodule for search roots

a = float(input('Write number a: '))                        # Asked user a variable

b = float(input('Write number b: '))                        # Asked user b variable

c = float(input('Write number c: '))                        # Asked user c variable

discrim = b ** 2 - 4 * a * c                                # Standart formula for search discriminant

print('discriminant = {}'.format(discrim))                  # Print this discriminant

if discrim > 0:                                             # If discriminant more 0
    
    print('The equation have two root')                     # Then print message about equation have two root
    
    root1 = round((-b + math.sqrt(discrim)) / (2 * a), 2)   # Standart formula for calculate first root
   
    root2 = round((-b - math.sqrt(discrim)) / (2 * a), 2)   # Standart formola for calculate second root
    
    print('root1 = {}, root2 = {}'.format(root1, root2))    # Print result two root
   
elif discrim == 0:                                          # If discriminant equally 0
    
    print('The equation have one root')                     # Then print message about equation have one root 
    
    root = round(-b / (2 * a), 2)                           # Standart formula for search one root
    
    print('root = {}'.format(root))                         # Print result one root

else:
    
    print('This equation not have roots')                   # Else print message about equations not have roots
    