# FastAPI + React integration

This demonstration displays how to integrate FastAPI or really any backend
with a React project (either using webpack or Vite). The purpose of this
is so that, insted of using JWTs, you are able to send HttpOnly stateful
session backed cookies to the client by delivering an HTML file from the
server rather than from a different domain.

The purpose is security, bottom line.

### Usage

Clone the frontend technologies. As shown below

```bash
git clone git@github.com:multiple-react-repo-for-fastapi/unauthenticated-react-webpack.git frontend
git clone git@github.com:multiple-react-repo-for-fastapi/authenticated-react-vite.git frontend
```

> **Note**
> The unauthenticated portion is a webpack + Babel project and the authenticated portion
> is uses Vite + SWC using TypeScript. They demonstrate how to integrate with either
> technology, but it's not recommended to use webpack -- based on my knowledge -- due to
> slower builds, and the JS ecosystem is generally moving away from webpack as 
> alternatives grow more mature.

For more info to deploy Vite + React from the backend, follow their guide:
https://vitejs.dev/guide/backend-integration.html

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
