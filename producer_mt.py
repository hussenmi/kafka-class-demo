from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', acks='all')

topics = ['topic_1', 'topic_2', 'topic_3']

for topic in topics:
    for i in range(10):
        message = f"message {i} for {topic}".encode('utf-8')
        future = producer.send(topic, value=message)
        result = future.get(timeout=10)
        print(f"Message {i} sent to {topic} in partition {result.partition} at offset {result.offset}")

producer.close()
