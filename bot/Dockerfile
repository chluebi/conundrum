FROM python:3.10-slim

WORKDIR /bot

RUN pip install pipenv

COPY Pipfile ./

RUN pipenv install --deploy --ignore-pipfile

COPY . /bot

CMD ["pipenv", "run", "python", "bot.py"]