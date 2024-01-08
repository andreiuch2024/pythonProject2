def multiplay(nuber_1, number_2):
    print('Функцию вызвали с параметрами', nuber_1, number_2)
    if isinstance(nuber_1, int):
        value = nuber_1 * number_2
        return value
    return "error"
print(multiplay(nuber_1='привет! ', number_2=27))