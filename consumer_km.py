from kafka import KafkaConsumer

consumer = KafkaConsumer('keyed_topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', group_id='keyed_topic_group')

for message in consumer:
    key = message.key.decode('utf-8') if message.key else None
    print(f"Received message with key {key}: {message.value.decode('utf-8')} from partition {message.partition}")

consumer.close()
