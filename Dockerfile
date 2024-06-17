FROM python:3.10


SHELL ["/bin/bash", "-c"]


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash crm_ && chmod 777 /opt /run

WORKDIR /crm_

RUN mkdir /crm_/static && mkdir /crm_/media && chown -R crm_:crm_ /crm_ && chmod 755 /crm_

COPY --chown=crm_:crm_ . .


RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev


USER crm_

CMD ["gunicorn","-b","0.0.0.0:8001","root.wsgi:application"]

