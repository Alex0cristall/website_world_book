from datetime import datetime


def func(n: int):
    return n**2


num = int(input("Введите число: "))
print(func(num))


def count_char_in_name(name: str):
    return len(name)


name_user = input("Введите ваше имя: ")
print(count_char_in_name(name_user))


print(datetime.now())
