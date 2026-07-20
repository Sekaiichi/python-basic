# 4. Написать функцию, которая принимает список, состоящий из объектов разных типов, и возвращает словарь, где:
# ключи — типы данных объектов;
# значения — списки объектов соответствующего типа.

def group_by_type(items):
    result = {}

    for item in items:
        item_type = type(item)

        if item_type not in result:
            result[item_type] = []

        result[item_type].append(item)

    return result


data = [1, "Python", 2.5, True, 10, "Hello", False, 3.14, [1, 2]]

print(group_by_type(data))