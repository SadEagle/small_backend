# Описание

Данный проект представляет из себя пример бэкенда с использованием FastAPI.

Реализованные составляющие проекта:
- [x] FastAPI
- [x] SQLAlchemy ORM + Pydantic
- [x] Pytest
- [x] Alembic migrations
- [x] Docker/Compose
- [x] Async
- [ ] Logs

# Запуск

## Запуск программы:
```
docker compose up
``` 

Для работы с API необходимо запустить alembic скрипт

- Инициализация базы данных с alembic:
```
docker exec *название_backend_контейнера* uv run alembic upgrade head 
```

- Запуск тестов pytest:
```
docker exec *название_backend_контейнера*  uv run pytest
```
