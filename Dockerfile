FROM python:3
RUN pip install flask
RUN pip install flask_restful
WORKDIR /
COPY . .
ENTRYPOINT [ "python" ]
CMD [ "./app.py" ]