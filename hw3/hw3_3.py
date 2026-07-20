# Написать функцию, которая создаёт абсолютный путь к файлу.
#
# Позиционные аргументы:
#
# название диска,
# неограниченное количество папок,
# имя файла (без расширения).
#
# Ключевые аргументы:
# ext — расширение файла,
# sep — разделитель (по умолчанию '/').
#
# Пример:
# full_path('c:', 'work', 'python', 'function', 'main', ext='py') ➜ 'c:/work/python/function/main.py'

def full_path(disk, *parts, ext, sep="/"):
    file_name = parts[-1]
    folders = parts[:-1]

    file_name = file_name + "." + ext.lstrip(".")

    return sep.join((disk, *folders, file_name))


result = full_path(
    "c:",
    "work",
    "python",
    "function",
    "main",
    ext="py"
)

print(result)