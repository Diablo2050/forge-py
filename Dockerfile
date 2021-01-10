FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app
RUN pip install -r /app/req.txt
WORKDIR /app
EXPOSE 5050
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]
