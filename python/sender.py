import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='I am sending to you ---')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='The message!!!')
print(" [x] Sent 'Hello World!'")
connection.close()
