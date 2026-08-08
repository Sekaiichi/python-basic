# ДЗ на тему урока - Базовые типы данных

# Задание 4
# Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа
num_to_rome_str = input(
    "Введите целое положительное число для перевода в римское число (не более 3999): "
)

print(int(num_to_rome_str))
if int(num_to_rome_str)>3999:
    print('Введено слишком большое число')
    exit()

rome_4th_dict = {'1': 'M', '2': 'MM', '3': 'MMM'}
rome_3th_dict = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
rome_2th_dict = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
rome_1th_dict = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
rome_whole_dict = {1: rome_1th_dict,2: rome_2th_dict,3: rome_3th_dict,4: rome_4th_dict}
rome_num = ''
inc_num = 0
for n in range(num_to_rome_str.__len__(),0,-1):
    rome_num += rome_whole_dict[n][num_to_rome_str[inc_num]]
    inc_num+=1
print(rome_num)