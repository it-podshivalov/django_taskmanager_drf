# django_taskmanager_drf

### Шаги для запуска: ### 

1. Запустите Docker

1. Убедитесь, что порты 5432, 8000 не заняты, если заняты - освободите

2. В командной строке перейдите в директорию с проектом

3. Установите необходимые пакеты выполнив команду-  
`pip install -r requirements.txt`

4. Создайте Docker контейнер с postgres выполнив команду-  
`python create_DB.py`

5. Выполните миграцию структуры в базу данных выполнив команды-  
`python final_project/manage.py makemigrations`  
`python final_project/manage.py migrate`

6. Создайте начальные данные в базе данных выполнив команду-  
`python final_project/manage.py loaddata initial_data.json`

7. Зпапустите приложение выполнив команду-  
`python final_project/manage.py runserver`

### API вызовы ###

- POST-запрос с json-телом для создания задания  
http://localhost:8000/api/tasks/  
    Пример тела запроса в json формате -  
        `{"Name": "Finish the course","Executor": "admin"}`  

- GET-запрос на получение всех заданий  
http://localhost:8000/api/tasks/  

- GET-запрос на получение определенного задания  
http://localhost:8000/api/tasks/1

- PATCH-запрос с json-телом на изменение в задание  
http://localhost:8000/api/tasks/1/  
    Пример тела запроса в json формате -  
        `{"Description": "With pleasure"}`

- DELETE-запрос на удаление задания  
http://localhost:8000/api/tasks/1