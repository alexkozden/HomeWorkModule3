def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, 578, 'Капибара']
values_dict = {'a' : 'Пёс', 'b' : True, 'c' : 53}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Идеи закончились", 404]

print_params(*values_list_2, 42)