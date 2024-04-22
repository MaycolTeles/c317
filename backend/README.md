# c317

Rodar FE:

```bash
poetry run flet run -d -r --web --port 8080 main.py
```

Rodar BE:

```bash
./manage.py runserver
```

Rodar Redis:

```bash
docker run -p 6379:6379 -d redis:5
```
