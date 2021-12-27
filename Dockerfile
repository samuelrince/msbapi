FROM python:3.9-slim

ENV POETRY_VERSION=1.1.12

# Setup poetry
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

# Install project dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy whole project
COPY . .

EXPOSE 5000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
