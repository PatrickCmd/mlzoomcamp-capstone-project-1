FROM python:3.9.16-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["gateway.py", "proto.py", "./"]

EXPOSE 9696

# uvicorn gateway:app --host 0.0.0.0 --port 9696
ENTRYPOINT ["uvicorn", "gateway:app", "--host", "0.0.0.0", "--port", "9696"]
