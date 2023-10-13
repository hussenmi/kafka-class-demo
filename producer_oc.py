from kafka import KafkaProducer

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', acks='all')

# Number of messages to produce
num_messages = 30

# Set of keys to cycle through to interleave messages across partitions
keys = ["key1", "key2", "key3"]

for i in range(num_messages):
    key_choice = keys[i % len(keys)]
    message = f"Message {i} with {key_choice}".encode('utf-8')
    future = producer.send('keyed_topic', key=key_choice.encode('utf-8'), value=message)
    result = future.get(timeout=10)  # Wait for up to 10 seconds for acknowledgment
    print(f"Sent {message.decode('utf-8')} to partition {result.partition} at offset {result.offset}")

producer.close()
