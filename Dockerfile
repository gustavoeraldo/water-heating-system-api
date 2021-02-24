FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

COPY ./app /api

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]