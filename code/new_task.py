import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "hello world"

channel.basic_publish(exchange='',
                    routing_key='hello',
                    body=message，
                    properties=pika.BasicProperties(
                        delivery_mode = 2,#make message persistent
                    )
                    )
print("Sent %r"%(message,))
