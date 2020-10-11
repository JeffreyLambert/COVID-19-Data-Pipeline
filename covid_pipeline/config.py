import os
import pathlib
import covid_pipeline

ROOT_PATH = pathlib.Path(covid_pipeline.__file__).resolve().parents[1]

OUTPUT_PATH = os.path.join(ROOT_PATH, 'covid_data.csv')