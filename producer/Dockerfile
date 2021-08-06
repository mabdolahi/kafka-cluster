FROM python:3-alpine
# Installing kafka client
RUN apk add py3-pip && pip install kafka-python 

# Add  script
COPY . ./
CMD ["Input.txt"]
ENTRYPOINT [ "python", "/producer.py"]
