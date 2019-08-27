import os

import pytest
from pytma.DataSources import DataSourceError, download_tolstoy_novels, get_transcription_data

def test_novel_data():

    try:
        print("getting novels from test location " + os.getcwd())
        download_tolstoy_novels('pytma/data/cache/')
    except DataSourceError:
        pytest.fail("Unexpected DataSourceError ..")


def test_medical_data():
    try:
        get_transcription_data()
    except DataSourceError:
        pytest.fail("Unexpected DataSourceError ..")
