FROM docker.io/library/python:3.13.7-alpine3.21

# Install uv
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend
# Compile bytecode
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1

COPY ./uv.lock ./pyproject.toml ./pyproject.toml ./

RUN uv sync --frozen

COPY ./app ./app
COPY ./alembic.ini ./

CMD ["uv", "run", "fastapi", "run", "--workers", "4", "./app/main.py"]

EXPOSE 8000
