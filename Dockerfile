FROM python:3.9 AS compiler

# Enable stream in Django log
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m venv /app/venv/
ENV VIRTUAL_ENV="/app/venv/"
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt /app/requirements.txt
RUN pip install --progress-bar off -r /app/requirements.txt

COPY . /app/


ENV DJANGO_DEBUG=False
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic

EXPOSE 8008
CMD ["waitress-serve", "--port=8008", "--threads=10", "run:wsgi_app"]
