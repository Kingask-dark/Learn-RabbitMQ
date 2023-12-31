import pika
import sys
import os
import time

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.queue_declare("test",durable=True)
    print("[*] Waiting for messages.TO exit press CTRL+C")

    def callback(ch,method,property,body):
        print(f"[x] Recived {body.decode()}")
        time.sleep(body.count(b'.'))
        print('[x] Done')
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue = 'test',
        on_message_callback = callback
    )
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            print('Interrupt')
            sys.exit(0)
        except SystemExit:
            os._exit(0)
