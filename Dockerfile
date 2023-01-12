FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN  pip install -r /app/requirements.txt

COPY /venv/main.py /app/main.py

CMD [ "uvicorn", "main:app" , "--reload", "--host=0.0.0.0"]

