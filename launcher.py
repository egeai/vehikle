import subprocess


def start_services():
    try:
        # Starting Prefect agent (assuming local executor for simplicity)
        subprocess.Popen(["prefect", "agent", "start"])
        # ... rest of your launcher script
    except Exception as e:
        print(f"Error starting Prefect agent: {e}")

    # Starting Celery worker
    subprocess.Popen(["celery", "-A", "tasks.celery_tasks", "worker", "--loglevel=info"])

    # Starting Celery Beat
    subprocess.Popen(["celery", "-A", "tasks.celery_tasks", "beat", "--loglevel=info"])


if __name__ == "__main__":
    start_services()