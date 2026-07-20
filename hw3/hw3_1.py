# 1. Написать функцию, которая принимает неограниченное количество чисел в виде позиционных аргументов и ключевой аргумент — операцию над этими числами (сложение или умножение).
# Функция должна возвращать результат выполнения указанной операции.

def calculate(*numbers, operation):
    if operation == "+":
        result = 0

        for number in numbers:
            result += number

        return result

    elif operation == "*":
        result = 1

        for number in numbers:
            result *= number

        return result

    else:
        return "Неизвестная операция"


print(calculate(2, 3, 4, operation="+"))
print(calculate(2, 3, 4, operation="*"))