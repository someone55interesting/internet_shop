# create_admin.py

import os
from django.contrib.auth import get_user_model

# 1. Получаем данные для администратора из переменных окружения
# Мы используем os.environ.get(), чтобы читать эти данные
USERNAME = os.environ.get('DJANGO_SUPERUSER_USERNAME')
EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')
PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

User = get_user_model()

if not all([USERNAME, EMAIL, PASSWORD]):
    # Если данные не заданы (как будет после первого запуска), просто выходим
    print("Переменные окружения для создания администратора не заданы. Пропускаем.")
else:
    # 2. Проверяем, существует ли пользователь с таким именем
    if not User.objects.filter(username=USERNAME).exists():
        
        # 3. Создаем суперпользователя
        User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
        print(f"Суперпользователь '{USERNAME}' успешно создан.")
        
        # 4. Удаляем переменные окружения после создания (очень важно для безопасности!)
        del os.environ['DJANGO_SUPERUSER_PASSWORD']
        del os.environ['DJANGO_SUPERUSER_USERNAME']
        del os.environ['DJANGO_SUPERUSER_EMAIL']
    else:
        print(f"Суперпользователь '{USERNAME}' уже существует. Пропускаем создание.")