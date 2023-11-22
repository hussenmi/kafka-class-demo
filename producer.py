from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', acks='all')

print("We are assuming that there is only one topic and one partition per topic.\n")
for i in range(5):
    message = f"message {i}".encode('utf-8')
    future = producer.send('my_topic', value=message)
    result = future.get(timeout=10)  # Wait for up to 10 seconds for acknowledgment
    print(f"Message {i} sent to partition {result.partition} at offset {result.offset}")
producer.close()