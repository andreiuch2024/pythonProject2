# Цикл for ("для каждого элемента")
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
print('Выход из цикла')

zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
letters_count = 0
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
    letters_count += len(animal)
    pass
print('Всего букв', letters_count)

# принудительный останов цикла - break
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
print('Выход из цикла')

# опция else для цикла
zoo_pets = ['lion', 'elephant', 'monkey', 'skunk', 'horse']
for animal in zoo_pets:
    print('Сейчас переменная animal указывает на ', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет....')
print('Выход из цикла')

# пропуск остатка цикла - continue
zoo_pets = ['lion', 'skunk', 'elephant', 'monkey', 'horse']
for animal in zoo_pets:
    if animal == 'skunk':
        continue
    print('у нас в руках', animal)
print('Выход из цикла')

# полный пример

zoo_pets = ['lion', 'monkey', 'skunk', 'elephant', 'horse']
for animal in zoo_pets:
    if animal == 'skunk':
        print('Фууу...')
        continue
    print('Сейчас переменная animal указывает на ', animal)
    if animal == 'elephant':
        print('Нашли слона! :)')
        break
    print('Это не слон....')
else:
    print('Тут слона нет...')
print('Выход из цикла')

# изменять содержимое последовательности, по которой проходит цикл, небезопасно
