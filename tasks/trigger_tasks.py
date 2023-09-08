from celery_tasks import run_flow


def trigger_csv_ingestion(src_path):
    run_flow.delay(source_type="csv", src_path=src_path)


def trigger_web_scraping(src_url):
    run_flow.delay(source_type="web", src_path=src_url)


if __name__ == "__main__":
    # This can be replaced with more advanced logic, CLI arguments, etc.
    trigger_csv_ingestion("../data/raw/data.csv")
