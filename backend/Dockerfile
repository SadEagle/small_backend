FROM docker.io/library/ubuntu:25.10

RUN apt update && apt install -y python3.14 curl
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend
COPY ./uv.lock ./pyproject.toml ./
RUN uv sync --frozen --no-cache

COPY ./app ./app
CMD [ "/backend/.venv/bin/fastapi", "dev", "./app/main.py" ]

EXPOSE 8000
