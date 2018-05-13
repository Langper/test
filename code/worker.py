import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='hello')

print('waiting for message press CTRL+C')

def callback(ch,method,properties,body):
    print("received %r"%(body,))
    time.sleep(body.count('.'))
    print("Done")

#告诉 RabbitMQ ，再同一时刻，不要发送超过1条消息给一个工作者（worker），直到它已经处理了上一条消息并且作出了响应
channel.basic_qos(prefetch_count=1)

channel.basic_consume(
                        callback,
                        queue='hello',
                        #no_ack=True#关闭响应机制
                    )
channel.start_consuming()
