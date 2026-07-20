# Дана строка текста (или введённая через консоль). Программа должна вернуть новую строку, в которой порядок слов будет обратным.
# Пример:
# "Python is really cool" → "cool really is Python".

text = input("Введите строку: ")

words = text.split()
words.reverse()
result = " ".join(words)

print(result)


