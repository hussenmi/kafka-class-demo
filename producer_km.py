from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', acks='all')

for i in range(30):  # Sending 30 messages
    key = f"key_{i % 3}".encode('utf-8')  # This will produce three unique keys: key_0, key_1, and key_2
    message = f"message {i} with {key.decode('utf-8')}".encode('utf-8')
    future = producer.send('keyed_topic', key=key, value=message)
    result = future.get(timeout=10)
    print(f"Message {i} with key {key.decode('utf-8')} sent to partition {result.partition} at offset {result.offset}")

producer.close()
