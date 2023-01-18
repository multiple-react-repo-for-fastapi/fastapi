# FastAPI + Django ORM Template

A GitHub template to quickly get a FastAPI project
that needs an awesome ORM up and running.

If you only need the Django ORM to write scripts,
feel free to simply use https://github.com/Andrew-Chen-Wang/django-orm-template
which does not include FastAPI.

Includes support for:
- Either SQLite or PostgreSQL
- Pre-commit

### Usage

To get started, run:

```bash
pip install -r requirements/local.txt
```

To run tests, run `pytest tests/`

To run the application:

```bash
python main.py run --reload --settings=local --log-level=debug
```

You can test FastAPI with our default view by going to http://127.0.0.1:5000/hello

To run management commands such as `makemigrations` and `migrate`:

```bash
python manage.py makemigrations core && python manage.py migrate
```

You can still run a script by adding a click command in [`main.py`](./main.py)

### Credit and License

This repository is based on the repository
by [@dancaron](https://github.com/dancaron/Django-ORM)
and reuses much of the code from https://github.com/Andrew-Chen-Wang/django-orm-template.

This repository is a quick template repository that I personally use.

This repository is licensed under the Apache 2.0 license
which can be found in the [LICENSE](./LICENSE) file.
