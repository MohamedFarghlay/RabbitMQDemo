using System;
using RabbitMQ.Client;
using System.Text;

namespace Producer
{
    public static class Sender
    {
        public static void Send()
        {
            var factory = new ConnectionFactory() { HostName = "localhost" };
            using (var connection = factory.CreateConnection())
            using (var channel1 = connection.CreateModel())
            {
                channel1.QueueDeclare(queue: "hello",
                    durable: false,
                    exclusive: false,
                    autoDelete: false,
                    arguments: null
                    );
                string message = "Hello, World!";
                var body = Encoding.UTF8.GetBytes(message);
                channel1.BasicPublish(exchange: "",
                    routingKey: "hello",
                    basicProperties: null,
                    body: body);

                Console.WriteLine(" [x] Send {0}",message);
            }
            Console.WriteLine(" Press [enter] to exit");
            Console.ReadLine();
        }  
    }
}
