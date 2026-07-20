# 3.Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов.

numbers = [1, 2, 2, 3, 1, 4, 3, 5]

result = []

for number in numbers:
    if number not in result:
        result.append(number)

print(result)


