FROM tiangolo/uwsgi-nginx-flask:python3.8
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var_d/www_d/app/static
COPY ./requirements.txt /var_d/www_d/requirements.txt
RUN pip install -r /var_d/www_d/requirements.txt