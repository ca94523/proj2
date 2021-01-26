# proj2

run in local shell:
exec gunicorn -k egg:meinheld#gunicorn_worker -c gunicorn_conf.py app.main:app