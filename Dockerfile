FROM python:3
COPY . /app
WORKDIR /app
RUN pip install flask gunicorn requests
EXPOSE 8080
ENV SERVER_PATH=https://fakesalty.baichuan.li
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]

