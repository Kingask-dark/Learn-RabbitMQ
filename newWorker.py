import pika
import os
import sys
import time

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare('task_queue',durable=True)
    print('[*] Waiting for message. To exit press CTRL+C')

    def callback(ch,method,properties,body):
        print(f"[x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print("[x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue',on_message_callback=callback)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)