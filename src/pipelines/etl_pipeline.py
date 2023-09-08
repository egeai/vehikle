import prefect
from prefect import task, Flow, Parameter
from datetime import datetime

from prefect import task, Flow
from ..extractors.extractor_factory import ExtractorFactory


logger = prefect.context.get("logger")


@task(max_retries=3, retry_delay=datetime.timedelta(minutes=1))
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
with Flow("Vehikle Data Ingestion Pipeline") as flow:
    logger.info("Getting source of data.")
    source_type = Parameter("source_type")
    src_path = Parameter('src_path')

    raw_data = extract_data(source_type=source_type, path_or_url=src_path)
    transformed_data = transform(raw_data)
    load(transformed_data)

flow.register(project_name="VehikleProject")

flow.run(source_type="csv", src_path='../data/car_data.csv')
# or
flow.run(source_type="web", src_path='https://example.com/data_source')

# Start Prefect server:
# prefect server start
# Start Prefect Agent to execute the flow runs (in another terminal)
# prefect agent local start

