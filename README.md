# proj2

run in local shell:
exec gunicorn -k egg:meinheld#gunicorn_worker -c gunicorn_conf.py app.main:app

run in docker:
docker run --rm --cpus="2" --memory=2g -d  -p 8000:8000/tcp proj2:latest