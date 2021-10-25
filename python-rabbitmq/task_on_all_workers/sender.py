import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = 'Hellow world!!!'

channel.basic_publish(
    exchange='logs', 
    routing_key='', 
    body=message,
)

print(" [x] Sent %s" % message)

connection.close()