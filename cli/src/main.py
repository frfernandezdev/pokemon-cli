import pika
from modules.core.application import PokemonCLI


def rabbit_mq(self):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="hello")
    channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")

    print("[X] Send 'Hello World!'")

    connection.close()


def main():
    PokemonCLI().run()


if __name__ == "__main__":
    main()
