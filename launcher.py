import subprocess


def start_services():
    # Starting Prefect agent (assuming local executor for simplicity)
    subprocess.Popen(["prefect", "agent", "start"])

    # Starting Celery worker
    subprocess.Popen(["celery", "-A", "tasks.celery_tasks", "worker", "--loglevel=info"])

    # Starting Celery Beat
    subprocess.Popen(["celery", "-A", "tasks.celery_tasks", "beat", "--loglevel=info"])


if __name__ == "__main__":
    start_services()