# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

string_list = input('Write your random text with split: ').split(' ')    # Write random first text 

sub_string = input('Write another random text for check second entry: ') # Write random second text for checking

def find_second_index(str_list, str):                                    # Create function for find second entry 
    
    '''Function for find second entry'''                                 # Function comment
    
    indexes = []                                                         # Create empty list
    
    if str_list.count(str) < 2:                                          # if count entry less 2
        
        return -1                                                        # Return -1
    
    else:                              
        
        for item in range(0, len(str_list)):                             # Else sort through item in this range
            
            if str_list[item] == str:                                    # if item in str_list equally str
                
                indexes.append(item)                                     # Add item in list indexes
                
            if len(indexes) == 2:                                        # if length list indexes equally 2
                
                return indexes[1]                                        # return item number 1
            
print(find_second_index(string_list, sub_string))                        # Print result

