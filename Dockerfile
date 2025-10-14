FROM python:3.13-slim-bookworm AS base

WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./

FROM base AS dev
RUN uv sync --frozen --no-cache
COPY ./src/app app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9999", "--reload"]

FROM base AS test
ENV PYTHONPATH=/app
RUN uv sync --frozen --no-cache --dev
COPY ./src .
CMD ["uv", "run", "pytest", "."]