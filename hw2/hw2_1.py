# 1. Написать программу, которая получает на вход строку и возвращает словарь, где:
# ключи — символы из этой строки;
# значения — количество раз, сколько каждый символ встречается.
from unittest import result

string = input("Введите cтроку: ")

result = {}

for char in string :
    result[char] = result.get(char, 0) + 1

print(result)
