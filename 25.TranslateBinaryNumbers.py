# 25. Написать программу преобразования десятичного числа в двоичное.

# a = int(input('Введите любое число: '))     # Asked user write number a

# result = []                                 # Create empty list result

# while a:                                    # While a

#     result.append(a % 2)                    # Add calculating the remainder number

#     a //= 2                                 # Add calculating the whole part number

# result.reverse()                            # Used function revers

# print(result)                               # Print this result number

# --------------------------------------------------------------------------------------------------

# number = int(input('Введите любое число: ')) # Asked user write number      

# print(bin(number))                           # Used Built-in library bin

# --------------------------------------------------------------------------------------------------

n = int(input('Write number n: '))            # Asked user write number n

binary_number = []                            # Create empty list

while n >= 1:                                 # While this number n more or equally 1
    
    binary_digits = n % 2                     # Calculating the remainder
    
    n = n // 2                                # Next calculate the whole part
    
    binary_number.append(binary_digits)       # And add this number in empty list
    
print('First number: ', binary_number)        # Print this list

reverse_number = binary_number[::-1]          # Next step do reverse this list

print('Reverse number: ', reverse_number)     # Print reverse list

for item in reverse_number:                   # Sort through item in reverse list
    
    print(item, end='')                       # Print items in the forms numbers