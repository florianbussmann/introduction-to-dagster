import csv

import requests
from dagster import DagsterType, In, Out, TypeCheck, get_dagster_logger, job, op


def is_list_of_dicts(_, value):
    return isinstance(value, list) and all(
        isinstance(element, dict) for element in value
    )


def simple_data_frame_type_check(_, value):
    if not is_list_of_dicts(_, value):
        return TypeCheck(
            success=False,
            description=f"SimpleDataFrame should be a list of dicts, got {type(value)}",
        )

    return TypeCheck(
        success=True,
        description="SimpleDataFrame summary statistics",
        metadata={
            "n_rows": len(value),
            "n_cols": len(value[0].keys()) if len(value) > 0 else 0,
            "column_names": str(list(value[0].keys()) if len(value) > 0 else []),
        },
    )


SimpleDataFrame = DagsterType(
    name="SimpleDataFrame",
    type_check_fn=simple_data_frame_type_check,
    description="A naive representation of a data frame, e.g., as returned by csv.DictReader.",
)


@op(out=Out(SimpleDataFrame))
def download_cereals():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return [row for row in csv.DictReader(lines)]


@op(ins={"cereals": In(SimpleDataFrame)})
def find_sugariest(cereals):
    sorted_by_sugar = sorted(cereals, key=lambda cereal: cereal["sugars"])
    get_dagster_logger().info(f'{sorted_by_sugar[-1]["name"]} is the sugariest cereal')


@job
def serial():
    find_sugariest(download_cereals())
