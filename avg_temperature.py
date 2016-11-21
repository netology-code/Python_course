# открытие файла
# .strip() - удаление пробелов с обоих сторон текста
# ' aaabb    \n\r\t'.strip() -> 'aaabb'

# Расширение списка
# a = [1, 2, 3]
# b = [7, 8, 9]
# "hello"
# a.append(b)
# [1, 2, 3, [7, 8, 9]]
# a.append(c)
# [1, 2, 3, "hello"]
# a.extend(b)
# [1, 2, 3, 7, 8, 9]

temperature = []

# эта конструкция, чтобы открывать файлы
# она вам сама их потом закроет
with open('temperature.txt') as t:
	for line in t:
		temperature.append(int(line))

print(temperature)

avg = sum(temperature)/len(temperature)

temperature_deviation = []

for t in temperature:
	temperature_deviation.append(t - avg)

#символ перенос строки: \n
print('Средняя температура \nВ Нижнем Новгороде:', avg)

with open('average_temperature.txt', 'w') as t_average_file:
	t_average_file.write("%.2f" % avg)

with open('temperature_deviation.txt', 'w') as t_deviation_file:
	for t in temperature_deviation:
		t_deviation_file.write("%.2f\n" % t)