def test():
    a = 5
    b = 3
    if a > 4:
       print('res_a =', a)
    if b < 4:
        print('res_b =', b)
    else:
      print('Выход')
test()

def test2(a, b, c):
    for res in a, b, c:
        print('результат =', res)
test2(2, 4, 6)

def test(a, b, c):
    print('результат =', ((a + b + c) ** 2))
test(10, 20, 4)






