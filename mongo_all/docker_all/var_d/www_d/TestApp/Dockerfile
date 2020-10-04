FROM tiangolo/uwsgi-nginx-flask:python3.8-2020-08-16
ENV STATIC_URL /static
ENV STATIC_PATH /var_d/www_d/app/static
COPY ./requirements.txt /var_d/www_d/requirements.txt
RUN pip install -r /var_d/www_d/requirements.txt