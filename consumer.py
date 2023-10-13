from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

for message in consumer:
    print(f"Message: {message.value.decode('utf-8')}, Partition: {message.partition}")
