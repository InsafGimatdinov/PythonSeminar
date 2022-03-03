# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = y = z = True

Check1 = not(x and y and z)

Check2 = (not x) or (not y) or (not z)

if Check1 == Check2:
    print(True)
else:
    print(False)