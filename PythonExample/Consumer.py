import sys
import os
import pika


def main():
    # establish a new connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", credentials=pika.PlainCredentials(username="dev", password="123")))

    # establish a channel
    channel = connection.channel()

    # create a queue in this channel
    channel_queue = channel.queue_declare("hello-queue")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue="hello-queue",
                          auto_ack=True,
                          on_message_callback=callback)

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
            os._exist(0)
