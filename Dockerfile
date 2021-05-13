FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/Webdornald/SynapseComponent.git

WORKDIR /home/SynapseComponent/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-)q9y#e2%u+*0=yiwe^y&wl=1^mwc74x&@@e27j#is6=b=p)^)s" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=config.settings.deploy && gunicorn config.wsgi --env DJANGO_SETTINGS_MODULE=config.settings.deploy --bind 0.0.0.0:8000"]