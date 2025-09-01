FROM docker.io/library/python:3.13.7-alpine3.21

# Install uv
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /backend
# Compile bytecode
# Ref: https://docs.astral.sh/uv/guides/integration/docker/#compiling-bytecode
ENV UV_COMPILE_BYTECODE=1

COPY ./uv.lock ./pyproject.toml ./
RUN uv sync --locked

COPY ./app ./app

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "./app/main.py"]
