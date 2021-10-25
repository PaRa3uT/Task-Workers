import dramatiq

from dramatiq.brokers.rabbitmq import RabbitmqBroker
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results.backends import RedisBackend
from dramatiq.results import Results


broker = RabbitmqBroker(host="localhost")
# broker = RedisBroker(host="localhost")

backend = RedisBackend()
broker.add_middleware(Results(backend=backend))

# dramatiq.set_broker(broker)
dramatiq.set_broker(broker)


@dramatiq.actor
def count_words():
    words_in_string = 'word_1 word_2, word_3'
    count = len(words_in_string.split(' '))
    print(f"There are {count} words at {words_in_string!r}.")


@dramatiq.actor(store_results=True)
def add(x, y):
    return x + y