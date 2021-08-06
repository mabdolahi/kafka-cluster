from kafka import KafkaProducer
import urllib.request,sys,configparser
from time import sleep,time
from json import dumps

def getPublicIP():
  # wait for Brokers to become Online!
  sleep(40)
  # Defining to read variables from file
  config = configparser.ConfigParser()
  # Reading varibales from Input file
  config.read(sys.argv[1])
  # Broker servers
  bootstrap_servers = config['settings']['brokers']
  # Defining interval for send data to broker
  send_interval = int(config['settings']['send_interval'])
  # Defining topic to send to
  topic = config['settings']['topic']

  # Definning producer and encode varibale
  producer = KafkaProducer(bootstrap_servers =  bootstrap_servers, value_serializer=lambda x: dumps(x).encode('utf-8'))
  
     
   # requesting public ip and send to it to Kafka Brokers for defined interval
  while True:
      
      try:
         
         external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
         #print(external_ip) 
         
         # it is tme to send to kafka broker 
    
         producer.send(topic, value=external_ip)
         sleep(send_interval - time() % send_interval)
     
      except KeyboardInterrupt:
          
         print('\n The Process has been Canceled by User')
         sys.exit(0)
          
getPublicIP()
