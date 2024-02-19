FROM python:3.7-alpine
WORKDIR /app
COPY  requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .
CMD [ "python","restapi.py" ]