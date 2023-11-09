import pika

def flask_queue(task):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()

    channel.queue_declare(queue="test",durable = True)
    print(task)

    channel.basic_publish(
        exchange = "",
        routing_key = 'test',
        body = task,
        properties= pika.BasicProperties(
            delivery_mode = pika.DeliveryMode.Persistent
        )
    )

    print(f"[x] Received {task}")
    connection.close()