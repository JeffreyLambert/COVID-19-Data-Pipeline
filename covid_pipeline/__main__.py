import pathlib
from covid_pipeline.etl import Pipeline
from covid_pipeline.config import OUTPUT_PATH


if __name__ == '__main__':

    etl = Pipeline()

    etl.retrieve_current()

    etl.clean_dates()

    etl.write_csv(OUTPUT_PATH)
