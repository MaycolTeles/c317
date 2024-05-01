# c317

Rodar aplicação:

```bash
docker-compose -f docker-compose.prod.yml up -d --build
```

Parar aplicação:

```bash
docker-compose -f docker-compose.prod.yml down -v
```

Rodar FE:

```bash
poetry run flet run -d -r --web --port 3000 main.py
```

Rodar BE:

```bash
./manage.py runserver
```

Rodar Redis:

```bash
docker run -p 6379:6379 -d redis:5
```
