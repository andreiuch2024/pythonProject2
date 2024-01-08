def print_params(a=1, b='строка', c=True):
   print(a)
   print(a, b)
   print(a, b, c)
   print('длинная', b)

print_params()
print_params(2,'линия', c=False)
print_params(b=25, c=[1, 2, 3])


values_list = [7, 'wave', {'car wash'}]
values_dict = {'a': '7', 'b': 'seven', 'c': '(b - a)'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [500, 'car']
print_params(*values_list_2, 42)
