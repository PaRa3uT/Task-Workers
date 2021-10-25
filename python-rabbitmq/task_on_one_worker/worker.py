import sys
import os
import pika
import time


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello', durable=True)


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    def callback_manual_ack(ch, method, properties, body):
        print(" [x] Received %r" % body)
        time.sleep(10)
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)


#    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback_manual_ack)

    print(' [*] Waiting for messages. To exit press CTRL+C')
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