# Дана строка текста (или введённая через консоль). Программа должна вернуть словарь с четырьмя ключами:
# "гласные",
# "согласные",
# "цифры",
# "пунктуация".
# Значения — количество символов каждого типа в строке.

text = input("Введите строку: ")

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouyAEIOUY"
punctuation = ".,!?;:-—()[]{}\"'«»…"

result = {
    "гласные": 0,
    "согласные": 0,
    "цифры": 0,
    "пунктуация": 0
}

for symbol in text:
    if symbol in vowels:
        result["гласные"] += 1
    elif symbol.isalpha():
        result["согласные"] += 1
    elif symbol.isdigit():
        result["цифры"] += 1
    elif symbol in punctuation:
        result["пунктуация"] += 1

print(result)


