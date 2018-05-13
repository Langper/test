import pika
import time

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()
    # time.sleep(60)
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
    print("Send hello world")

    connection.close()

print("want to be 1!")

send_message()

print("want to execute immediately!")
