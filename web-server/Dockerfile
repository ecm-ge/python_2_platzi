FROM  python:3.10

WORKDIR /web-server
COPY requirements.txt /web-server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get update
RUN apt-get install nano -y

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]