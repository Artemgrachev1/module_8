def add_everything_up(a, b):
    try:
        s = a + b
    except TypeError as te:
        s = (str(a) + str(b))
        return s
    else:
        return round(s, 3)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))