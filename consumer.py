import pika
import time

def connect_to_rabbitmq():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='data_exchange', exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='data_exchange', queue=queue_name)
        return channel, queue_name
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")
        raise

def callback(ch, method, properties, body):
    print(f"Received message: {body}")

def consume_messages():
    retries = 5  # Number of retry attempts
    retry_delay = 5  # Delay between retries in seconds
    channel = None  # Initialize channel variable

    while retries > 0:
        try:
            channel, queue_name = connect_to_rabbitmq()
            print(f"Consumer connected to queue: {queue_name}")

            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

            print('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
        
        except KeyboardInterrupt:
            print('Consumer stopped by user.')
            break
        
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Failed to connect to RabbitMQ: {e}")
            retries -= 1
            if retries > 0:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries exceeded. Exiting.")
        
        finally:
            if channel:
                channel.close()

if __name__ == "__main__":
    consume_messages()
