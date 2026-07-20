# Даны три (или больше) списка с объектами.
# Программа должна создать новый список,
# содержащий все уникальные элементы — каждый объект встречается только один раз.

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
list_3 = [1, 6, 7, 8]

all_elements = list_1 + list_2 + list_3

result = []

for element in all_elements:
    if element not in result:
        result.append(element)

print(result)


