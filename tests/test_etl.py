import pytest
import pandas as pd
from covid_pipeline.etl import Pipeline
from pandas.api.types import is_datetime64_dtype


@pytest.fixture
def create_object():
    return Pipeline()


def test_retrieve_current(create_object):
    etl = create_object
    etl.retrieve_current()
    assert etl.resp is not None
    assert etl.resp.status_code == 200


def test_retrieve_historical(create_object):
    etl = create_object
    etl.retrieve_historical()
    assert etl.resp is not None
    assert etl.resp.status_code == 200


def test_retrieve_status(create_object):
    etl = create_object
    etl.retrieve_status()
    assert etl.resp is not None
    assert etl.resp.status_code == 200


def test_clean_dates(create_object):
    etl = create_object
    etl.df = pd.DataFrame({'dates': [20201009, 20201019]})
    etl.clean_dates()
    assert is_datetime64_dtype(etl.df.dates)

