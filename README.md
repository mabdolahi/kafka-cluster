# kafka-cluster

This is a simple Kafka cluster. The cluster contains 3 kafka nodes and 3 zookeeper nodes. The cluster comes up with single docker compose file. The nodes are communicating throgh customized bridge network. You can connect to the kafka brokers from docker host or outside of docker host.

*Please keep in mind, this is not recommend for production because of the lack of authentications. You must setup authentication for kafka brokers and zookeeper. to persist data you must include a volume to mount to the containers.

The kafka producer is implemented using python container. It will send public ip of the host to the broker every 5 second. The kafka consumer is implemented using python container. It will recive the messsage from kafka producess.

The Producer and consumer settings can be passed via input.txt file, in order to change your setting.
