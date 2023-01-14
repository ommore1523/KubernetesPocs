FROM python
COPY database.py  /
COPY server.py  /
COPY requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]

