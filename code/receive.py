import pika
import time
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='hello')
print('waiting for messages.To exit press Ctrl + C')

def done():
    time.sleep(60)
    print("first try differet!")
def callback(ch,method,properties,body):
    # print("Recevied %r"%(body,))
    done()

channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()
