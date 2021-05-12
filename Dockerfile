FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Webdornald/SynapseComponent.git

WORKDIR /home/SynapseComponent/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-)q9y#e2%u+*0=yiwe^y&wl=1^mwc74x&@@e27j#is6=b=p)^)s" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]