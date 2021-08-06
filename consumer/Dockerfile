FROM python:3-alpine
# Installing kafka client
RUN apk add py3-pip && pip install kafka-python 
# Add  script and input file
COPY . ./ 

CMD ["Input.txt"]
# -u is for seending print output unbuffered to the docker logs
ENTRYPOINT [ "python", "-u", "/consumer.py"]
