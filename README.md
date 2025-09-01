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

Для работы с API необходимо запустить alembic скрипт

- Инициализация ьазы данных с alembic:
```
docker exec -it *название_backend_контейнера* uv run alembic upgrade head 
```

- Запуск тестов pytest:
```
docker exec -it *название_backend_контейнера*  uv run pytest
```
