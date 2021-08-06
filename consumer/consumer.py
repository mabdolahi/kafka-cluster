from kafka import KafkaConsumer,TopicPartition
from json import loads
from time import sleep,time
import sys,configparser,time



def kafka_consumer():
  # waiting for brokers to become Online, so we can avoid NoBrokerAvailible warning
  time.sleep(50)
  # Definning to read variables from file
  config = configparser.ConfigParser()
  config.read(sys.argv[1])
  bootstrap_servers = config['settings']['brokers']
  topic = config['settings']['topic']
  consume_interval = int(config['settings']['wait'])
  
  # defining consumer
  consumer = KafkaConsumer(topic, bootstrap_servers = bootstrap_servers, auto_offset_reset='latest', enable_auto_commit=False, auto_commit_interval_ms=5000, group_id='PublicIP', value_deserializer=lambda x: loads(x.decode('utf-8')))
  
  
 
  # it is time to consume messages from kafka brokers
  while True: 
      
      try:
         
         for message in consumer:
             # seek to the last offset
             consumer.seek_to_end()
             # commit the offset
             consumer.commit()
             
            # print(message.offset)
             msg = message.value
             print(msg)
             
             time.sleep(consume_interval)
          
            
      except KeyboardInterrupt:
          
         print('\n The Process has been Canceled by User')
         sys.exit(0)
         
  
kafka_consumer()
