import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)

channel.basic_publish(
    exchange='', 
    routing_key='hello', 
    body='Hellow world!!!',
    properties=pika.BasicProperties(
        delivery_mode = 2, # make message persistent
))

print(" [x] Sent 'Hellow world!!!'")

connection.close()