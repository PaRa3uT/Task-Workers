import sys
import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = 'Hellow world!!!'

channel.basic_publish(
    exchange='topic_logs', 
    routing_key=routing_key, 
    body=message,
)

print(" [x] Sent %r:%s" % (routing_key, message))

connection.close()