import os.path

# взяли абсолютный путь к текущему файлу
# отбросили имя файла, оставили только имя пки
local_path = os.path.dirname(os.path.realpath(__file__))
# объединили путь до папки с программой с файлом 'countries.txt'
countries_path = os.path.join(local_path, 'countries.txt')

print(countries_path)
with open(countries_path) as countries:
	for country in countries:
		print(country)