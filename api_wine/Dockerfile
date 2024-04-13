FROM python:3.11-slim

ARG APP_PATH=/api_wine/
ARG APP_USER=api_wine
WORKDIR ${APP_PATH}

RUN apt-get update && apt-get upgrade -y \
	&& rm -rf /var/lib/apt/lists/* \
	&& adduser --system --group --uid 1000 --home ${APP_PATH} ${APP_USER} \
	&& pip install --no-cache-dir 'poetry>=1.6' \
	&& poetry config virtualenvs.create false

COPY --chown=${APP_USER}:${APP_USER} api_wine/pyproject.toml api_wine/poetry.lock ./
COPY --chown=${APP_USER}:${APP_USER} api_wine/api_wine/ ./api_wine/
RUN touch README.md

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

USER ${APP_USER}

ENTRYPOINT [ "uvicorn", "--app-dir=api_wine/", "--host=0.0.0.0", "api:app" ]
