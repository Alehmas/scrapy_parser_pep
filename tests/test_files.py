import pytest

from pathlib import Path

BASE_DIR = Path(__name__).absolute().parent
MAIN_DIR = BASE_DIR / 'pep_parse'


@pytest.fixture
def results_dir():
    results_dir = [
        d for d in BASE_DIR.iterdir() if d.is_dir() and d.name == 'results'
    ]
    results_dir += [
        d for d in MAIN_DIR.iterdir() if d.is_dir() and d.name == 'results'
    ]
    return results_dir


def test_results_dir_exists(results_dir):
    assert len(results_dir), (
        'Folder /results not found'
    )


def test_csv_files(results_dir):
    csv_files = [
        file for file in results_dir[0].iterdir() if file.glob('*.csv')
    ]

    assert len(csv_files), (
        'No csv files were found in the results folder '
        'with the results of the parser.'
    )
    assert not len(csv_files) < 2, (
        'There should be two csv files in the results folder. '
        'Save to this folder the latest '
        'csv files with parsing results'
    )
    assert not len(csv_files) > 2, (
        'There are more than two files in the results folder. '
        'Leave in it two actual csv-files with parsing results.'
    )
