import pika

# establish a new connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", credentials=pika.PlainCredentials(username="dev", password="123")))

# establish a channel
channel = connection.channel()

# create a queue in this channel
channel_queue = channel.queue_declare("hello-queue")
channel_queue2 = channel.queue_declare("hello-queue2")

# create a new exchange to use queue within
channel_exchange = channel.exchange_declare("hello-exchange")

# bind queue to exchange
channel.queue_bind("hello-queue", "hello-exchange", 'hello')
channel.queue_bind("hello-queue2", "hello-exchange", 'hello2')

# publish a message
channel.basic_publish(exchange="hello-exchange",
                      routing_key="hello",
                      body="Hello RabbitMQ how are you?")

channel.basic_publish(exchange="hello-exchange",
                      routing_key="hello2",
                      body="this message sent from python to test queue 2")

print(" [x] Sent 'Hello from producer'")

connection.close()
