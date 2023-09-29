x = 2

try:
    print(x / 0)
except NameError:
    print('Undefind')
except ZeroDivisionError:
    print('dont divide by 0')
