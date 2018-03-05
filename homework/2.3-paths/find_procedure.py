# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    # ваша логика
    
import os.path
import chardet

def make_files_list(): 
  migrations_dir = os.path.join(current_dir, migrations)
  file_list = os.listdir(path=migrations_dir)
  return file_list

def sql_list(file_list):
  proper_files = list()
  for i in file_list:
    filter(lambda x: x.endswith('.sql'), files)  # only sql files 
    proper_files.append(i)
  return proper_files

def readable_files(file_name):
  with open(os.path.join(current_dir, migrations, file_name), 'rb') as l:
    info = l.read()
    result = chardet.detect(info)
    info = info.decode(result['encoding'])
  return info
  
def find_string(sql_list):
  file_list = sql_list
  while True: 
    search = input('Write your string: ') 
    files_inside = list() 
    for file_name in file_list: 
      if search in readable_files(file_name):
        files_inside.append(file_name)
        print(file_name)
    print('Всего: {0}'.format(len(files_inside)))
    file_list = files_inside
 
if __name__ == '__main__':
    find_string(sql_list(make_files_list()))
    
    pass
