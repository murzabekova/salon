# Salon

## Установка
1. Для запуска проекта нужен virtualenv созданный с помощью python3
2. Установите все по списку requirements.txt
3. В проекте : project=>settings.py загружен settings_local.py где мы сами прописываем нужный нам DB, по умолчанию в django стоит такая строчка:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
а также не забудьте добавить еще `DEBUG = True`.

## Проект
