BROKER_URL = 'pyamqp://guest:guest@localhost//'
RESULT_BACKEND = 'redis://localhost:6379/0'

from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    'run-every-ten-minutes': {
        'task': 'tasks.celery_tasks.run_flow',   # path to your task function
        'schedule': timedelta(minutes=10),
        'args': ("csv", "../data/car_data.csv")  # if your task function requires arguments
    },
}