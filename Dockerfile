FROM python:3.8
RUN pip install meinheld gunicorn flask
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
#COPY ./app /app
COPY ./config.py /config.py
#WORKDIR /app/
#ENV PYTHONPATH=/app

################################
## INSTALL R
COPY r_scripts /r_scripts
RUN chmod -R +x /r_scripts
RUN /r_scripts/install_r.sh
RUN /r_scripts/install_rpackage.sh
################################
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
################################
COPY ./app /app
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]
