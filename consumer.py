from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

for message in consumer:
    print(f"{message.value.decode('utf-8')} received from partition {message.partition} at offset {message.offset}")

consumer.close()
