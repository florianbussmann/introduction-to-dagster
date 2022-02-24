from dagster import job, op, get_dagster_logger

from cereal_serial_pipeline import download_cereals


@op
def hello_cereal():
    cereals = download_cereals()
    get_dagster_logger().info(f"Found {len(cereals)} cereals")


@job
def hello_cereal_job():
    hello_cereal()


if __name__ == "__main__":
    result = hello_cereal_job.execute_in_process()
