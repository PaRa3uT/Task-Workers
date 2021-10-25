import time
from celery import Celery


class Config:
    CELERY_BROKER_URL = 'pyamqp://localhost'
    result_backend = 'redis://localhost:6379/1'


app = Celery('tasks', broker=Config.CELERY_BROKER_URL)
app.config_from_object(Config)

print(app.conf.table(with_defaults=False, censored=True))

@app.task(bind=True)
def add(self, x, y):
    print(self.request.id)
    return x + y


@app.task
def add_delayed(x, y):
    time.sleep(10)
    return x + y
