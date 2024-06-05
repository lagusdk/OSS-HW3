FROM python

WORKDIR /app/

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD python main.py