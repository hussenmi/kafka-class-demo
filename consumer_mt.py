from kafka import KafkaConsumer

topics = ['topic_1', 'topic_2', 'topic_3']
consumer = KafkaConsumer(*topics, bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

for message in consumer:
    print(f"Received {message.value.decode('utf-8')} from {message.topic} in offset {message.offset}")
