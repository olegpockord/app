__Как запустить приложение__

Для начала нужно поставить виртуальное окружение и зайти в него  
Потом нужно загрузить requirements.txt
```
pip install -r requirements.txt
```
Для создания суперюзера
```
manage.py createsuperuser
```
Если миграции не выполнены:
```
manage.py makemigration
```
  
```
manage.py migrate
```
И запуск сервера
```
manage.py runserver
```
