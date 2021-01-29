FROM python:3.8
RUN pip install meinheld gunicorn flask
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./app /app
WORKDIR /app/
ENV PYTHONPATH=/app

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Meinheld
CMD ["/start.sh"]


