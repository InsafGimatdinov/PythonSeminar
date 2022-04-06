# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def get_input_int(arg_text):
    
    '''Get integer enter users'''
    
    while True:
        
        try:
            
            input_value = input(arg_text)
            
        except:
            
            print(f'Value ({input_value}) not is integer number')
            
def create_polynom(list_of_items):
    
    result = ''
    
    for item in range(len(list_of_items)):
        
        for k in range(len(list_of_items[item])):
            
            result += (f'{list_of_items[item][k]}')
            
            if k != 1: 
                
                result += 'x'
            
        if list_of_items[item][k] == 1:
            
            result += '+'
            
        if item == (len(list_of_items) - 1):
            
            result += (f'{random.randint(0, 101)} = 0')
    
    return result

degree = int(input('Write older degree of polynomial: '))

quant_of_items = degree 

items_of_polynomial = []

for item in range(quant_of_items):
    
    rand_ratio = random.randint(0, 101)
    
    items_of_polynomial.append([rand_ratio, degree - 1])
    
polynomial_str = create_polynom(items_of_polynomial)

print(items_of_polynomial)

print(polynomial_str)

with open('Task33_polynomial.txt', 'w') as f:
    f.write(polynomial_str)           