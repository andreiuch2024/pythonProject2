car_list = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
for stamp in car_list:
    print('Я езжу на автомобиле марки', stamp)
cars_count = 0
for stamp in car_list:
    cars_count += 10
    pass
print('Всего автомобилей', cars_count)

# Параметры
def print_params(color_car):
    print('Авто:', color_car)
my_car = [('BMW - red'), ('LADA - black')]
print('Цвета моих машин')
for color in my_car:
    print_params(color_car=color)
    print('Все правильно')


def print_params(color_car):
    color_car = 'BMW - red, LADA - black'
    print('Цвет авто:', color_car)


for color_car in range(2):
    print_params(color_car)
