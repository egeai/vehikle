from celery import Celery
from prefect import Flow
from src.pipelines.etl_pipeline import flow

app = Celery('tasks')
app.config_from_object('celery_config')


@app.task
def run_flow(source_type: str, src_path: str):
    flow.run(source_type=source_type, src_path=src_path)
