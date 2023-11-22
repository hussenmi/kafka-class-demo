from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', acks='all')

topics = ['topic_1', 'topic_2', 'topic_3']

print("We are assuming that there is only one partition per topic.\n")

for id,topic in enumerate(topics):
    for i in range(3):
        message = f"message {i+id*3} for {topic}".encode('utf-8')
        future = producer.send(topic, value=message)
        result = future.get(timeout=10)
        print(f"Message {i+id*3} sent to {topic} in partition {result.partition} at offset {result.offset}")

producer.close()
