FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./app /app
