import pika
import json
from faker import Faker
import time

# Initialize Faker for generating synthetic data
fake = Faker()

def connect_to_rabbitmq():
    # Establish connection to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='data_exchange', exchange_type='fanout')
    return channel

def produce_messages(channel):
    while True:
        # Generate synthetic temperature and humidity data
        message = {
            'timestamp': fake.date_time().isoformat(),
            'temperature': fake.pyfloat(min_value=-10, max_value=40, right_digits=2),
            'humidity': fake.pyfloat(min_value=20, max_value=80, right_digits=2)
        }
        
        # Publish message to RabbitMQ
        channel.basic_publish(exchange='data_exchange', routing_key='', body=json.dumps(message))
        print(f"Published message: {message}")
        
        # Sleep for 5 seconds before publishing the next message
        time.sleep(5)

if __name__ == "__main__":
    channel = connect_to_rabbitmq()
    produce_messages(channel)
