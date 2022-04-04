# 31. Составить список простых множителей натурального числа N.

number = int(input('Write number, please: '))     # Asked user write number

lst = []                                          # Create empty list

for item in range(2, number):                     # Sort through item in this range
    
    while number % item == 0:                     # While while an even value comes out
        
        number /= item                            
        
        lst.append(item)                          # Add to list this item
        
print(lst)                                        # Print this items in list