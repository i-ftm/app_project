FROM docker.arvancloud.ir/python:3.12.2
WORKDIR /app
COPY  ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY financial .
EXPOSE 8000
CMD [ "python" , "manage.py" , "runserver" ]