!warning on windows 10 default -P=prefork, don't run task

# Celery
python -m celery -A <tasks> worker -l INFO -E -c 10 -P gevent -n worker1
python -m celery -A <tasks> worker -l INFO -E -c 10 -P gevent -n worker2

# Flower
celery flower --port=5566
celery -A <proj> flower --address=127.0.0.6 --port=5566