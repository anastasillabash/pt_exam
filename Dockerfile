FROM python:3
WORKDIR /
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "./app.py" ]
