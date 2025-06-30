FROM python:3.10.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /maindir .

CMD [ "python", "main.py" ]