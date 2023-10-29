from datetime import timedelta

import prefect  # type: ignore
from prefect import task, flow, get_run_logger
from prefect.runtime import flow_run  # type: ignore

from ..extractors.extractor_factory import ExtractorFactory  # type: ignore

# logger = get_run_logger()


@task(retries=3, retry_delay_seconds=10000)
def extract_data(source_type: str, path_or_url: str):
    extractor = ExtractorFactory.get_extractor(source_type=source_type)
    if source_type == "csv":
        return extractor.extract(path_or_url)
    elif source_type == "web":
        return extractor.extract(path_or_url)
    else:
        return None


@task
def transform(data):
    # Transformation logic
    # Your transformation logic, like cleaning, enriching, etc.
    return "Transformed" + data


@task
def load(data):
    # Load the transformed data to its final destination, such as a database
    pass


# Define Flows
with flow(name="Vehikle Data Ingestion Pipeline") as flw:
    # logger.info("Getting source of data.")
    source_type = flow_run.parameters["source_type"]
    src_path = flow_run.parameters['src_path']

    raw_data = extract_data(source_type=source_type, path_or_url=src_path)
    transformed_data = transform(raw_data)
    load(transformed_data)

flw.register(project_name="VehikleProject")
# flw.run(source_type="csv", src_path='../data/car_data.csv')
# or
# flw.run(source_type="web", src_path='https://example.com/data_source')

# Start Prefect server:
# prefect server start
# Start Prefect Agent to execute the flow runs (in another terminal)
# prefect agent local start
