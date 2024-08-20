FROM python:3.12-slim
COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
