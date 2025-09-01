# Описание

Данный проект представляет из себя пример бэкенда с использованием FastAPI.

Реализованные составляющие проекта:
- [x] FastAPI
- [x] SQLAlchemy ORM + Pydantic
- [x] Pytest
- [x] Alembic migrations
- [x] Docker/Compose
- [ ] Logs
- [ ] Async

# Запуск

## Запуск программы:
```
docker compose up
``` 

Пользоваться API можно только после использования скрипта alembic

- Создание таблиц с alemblic:
```
docker exec -it *название_контейнера* uv run alembic upgrade head 
```

- Запуск тестов pytest:
```
docker exec -it *название_контейнера*  uv run pytest
```
