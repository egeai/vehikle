from celery import Celery  # type: ignore
# from prefect import flow  # type: ignore
from src.pipelines.etl_pipeline import flw  # type: ignore

app = Celery('tasks')
app.config_from_object('tasks.celery_config')
app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


@app.task
def run_flow(source_type: str, src_path: str):
    flw.run(source_type=source_type, src_path=src_path)
