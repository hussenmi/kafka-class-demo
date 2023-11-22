from kafka import KafkaConsumer

# Creating a Kafka consumer with auto offset commit disabled
consumer = KafkaConsumer('keyed_topic', bootstrap_servers='localhost:9092', 
                         auto_offset_reset='earliest', group_id='checkpoint_group', 
                         enable_auto_commit=False)

# Counter to limit the number of messages processed for demonstration
counter = 0

for message in consumer:
    print(f"Received {message.value.decode('utf-8')} from partition {message.partition} at offset {message.offset}")
    
    # Process the message (in this demo, we're just printing it)
    # After processing, we commit the offset
    consumer.commit()
    
    counter += 1
    if counter >= 3:  # Stop after processing 3 messages
        break

consumer.close()
