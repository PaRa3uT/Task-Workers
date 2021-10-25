import sys
import os
import pika
import time


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    result = channel.queue_declare(queue='', exclusive='True')
    queue_name = result.method.queue

    binding_keys = ['anonymous.info']

    for binding_key in binding_keys:
        channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)


    def callback(ch, method, properties, body):
        print(" [x] Received %r:%r" % (method.routing_key, body))

    channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
#            os_exit(0)
            pass