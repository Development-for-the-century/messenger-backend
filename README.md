## Запуск сервиса

### Установка зависимостей
Перед запуском убедитесь, что у вас установлен [uv](https://docs.astral.sh/uv/getting-started/installation/#pypi). Затем установите зависимости:

```bash
uv sync
```

Установить прекоммиты
```bash
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg
uv run pre-commit install --hook-type pre-push
```


### Запуск локально
Запустите сервис с помощью Uvicorn:

```bash
uv run uvicorn app.main:app --app-dir=src --host 0.0.0.0 --port 9999
```

### Запуск в докере

dev контейнер:

```bash
docker compose -f compose.dev.yaml up --build
```

test контейнер:
```bash
docker compose -f compose.test.yaml up --build
```

## Документация

```
http://localhost:9999/docs
```

Моковые данные для */api/login*:
```
{
  "username": "uname",
  "password": "test"
}
```