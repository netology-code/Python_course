# обращение к внешней переменной окружения
# Linux/Mac: export USER_NAME=Олег
# Windows: set USER_NAME=Олег

import os
username = os.environ['USER_NAME']
print('Привет,', username)