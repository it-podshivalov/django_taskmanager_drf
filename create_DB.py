import os
import time

DB_USER = "postgres"
DB_NAME = "TaskManager"
DB_PASSWORD = "postgrespw"
DB_HOST = "127.0.0.1"

# удаление существующего контейнера
os.system(f"docker rm --force My_Postgres")

time.sleep(2)

# создание Docker контейнера с postgres
os.system(
    f"docker run --name My_Postgres -p 5432:5432 -e POSTGRES_USER={DB_USER} -e POSTGRES_PASSWORD={DB_PASSWORD} -e POSTGRES_DB={DB_NAME} -d postgres:latest"
)
