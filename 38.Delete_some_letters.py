# Напишите программу, удаляющую из текста все слова содержащие "абв".

some_text = 'зафиксированная на забвения каком-либо материальном набвтеле человеческая мыслью Абв бабвгдэ абв'

splitted_text = some_text.split()

text_rem = some_text.replace('абв', '')

modified_text = []

for item in range(len(splitted_text)):
    
    if 'абв' in splitted_text[item].lower():
        
        continue
    
    else:
        
        modified_text.append(splitted_text[item])
        
print(modified_text)

string_modified_text = ' '.join(modified_text)

print(string_modified_text) 
