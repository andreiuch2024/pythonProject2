def test(a, b):
    return (a * 2 + b * 4) ** 2
res = test(5, 6)
print(res)

def test2(a, b, c):
    for res in a, b, c:
        print('результат =', res)
test2(2, 4, 6)

def test(a, b, c):
    print('результат =', ((a + b + c) ** 2))
test(10, 20, 4)






