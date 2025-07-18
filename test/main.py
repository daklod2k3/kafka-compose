from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import time

KAFKA_BROKER = 'localhost:9092'  # Change this if your broker runs elsewhere
TEST_TOPIC = 'test_topic'

# Produce a test message
def test_producer():
    try:
        producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
        future = producer.send(TEST_TOPIC, b'Test message from Python')
        result = future.get(timeout=10)
        print(f"✅ Message sent to {result.topic}:{result.partition} at offset {result.offset}")
        producer.close()
    except KafkaError as e:
        print(f"❌ Kafka producer error: {e}")

# Consume the test message
def test_consumer():
    try:
        consumer = KafkaConsumer(
            TEST_TOPIC,
            bootstrap_servers=KAFKA_BROKER,
            auto_offset_reset='earliest',
            consumer_timeout_ms=5000  # wait for 5s for message
        )
        print("📥 Waiting for messages...")
        for message in consumer:
            print(f"✅ Received: {message.value.decode('utf-8')} (offset {message.offset})")
            break  # stop after first message
        consumer.close()
    except KafkaError as e:
        print(f"❌ Kafka consumer error: {e}")

if __name__ == '__main__':
    print("🟢 Testing Kafka Producer...")
    test_producer()

    # Sleep briefly to ensure the broker has processed the message
    time.sleep(2)

    print("\n🟢 Testing Kafka Consumer...")
    test_consumer()
