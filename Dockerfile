#1. SELECT Python Image
FROM python:3.9.0

WORKDIR /home/

# Added this command below because of the cached data.
RUN echo 'testing1'
RUN echo 'testing2'
RUN echo 't7'
RUN echo 'ttttttttt'
######################################################

# 2. Bring Source codes from GitHub
# - By doing so, there's a 'berryland' DIR in home.
RUN git clone https://github.com/jeongwookim2022/berryland.git

WORKDIR /home/berryland/

# 3. Install libraries in requirements in this Django IMAGE.
RUN pip install -r requirements.txt

##################################################################################################
# Added this command below because of the cached data.
RUN pip install gunicorn

# Added this command below for MariaDB(external DB instead of Sqlite3).
RUN pip install mysqlclient

# Just for now to run this IMAGE for test.
# - It creates '.env' file with the SECRET KEY.

# Used Docker Secret
# - Deleted the command below.
# RUN echo "SECRET_KEY=~~~~~~~~~~~~~~" > .env
##################################################################################################

# 4. Connect DB.
# RUN python manage.py migrate
# -> Don't use 'sqlite3' anymore, but use 'MariaDB' which is external DB.
#    So, i'm using an external container. That means the command above won't work.
#    I will type the command above in CMD below.

# 7. Collect Static contents in Django and Synchronize them with Nginx container in PVS.
# RUN python manage.py collectstatic

# 5. EXPOSE 8000 port in this Django IMAGE.
EXPOSE 8000

# 6. Set commands to run a container from this IMAGE.
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# - By adding Gunicorn, the command above is replaced to 'Gunicorn command'.
# CMD ["gunicorn", "berryland.wsgi", "--bind", "0.0.0.0:8000"]

# Using 2 commands requires another way of typing like the code below.
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=berryland.settings.deployment && python manage.py migrate --settings=berryland.settings.deployment && gunicorn berryland.wsgi --env DJANGO_SETTINGS_MODULE=berryland.settings.deployment --bind 0.0.0.0:8000"]
