import os
import re
from pathlib import Path

import pytest
from pep_parse import pipelines
from scrapy.crawler import CrawlerProcess

try:
    from pep_parse.spiders.pep import PepSpider
except ModuleNotFoundError:
    raise AssertionError(
        'No `pep.py` file found in pep_parse.spiders directory',
    )


def test_run_scrapy(monkeypatch, tmp_path):
    mock_base_dir = Path(os.path.relpath(tmp_path))
    monkeypatch.setattr(pipelines, 'BASE_DIR', mock_base_dir)

    process = CrawlerProcess(settings={
        'LOG_ENABLED': False,
        'LOG_LEVEL': 'ERROR',
        'HTTP_CACHE': True,
        'HTTPCACHE_ENABLED': True,
        'ITEM_PIPELINES': {
            'pep_parse.pipelines.PepParsePipeline': 300,
        },
        'FEEDS': {
            mock_base_dir / 'results/pep_%(time)s.csv': {
                'format': 'csv',
                'fields': ['number', 'name', 'status'],
            },
        },
    })
    process.crawl(PepSpider)
    process.start()

    dirs = [
        directory.name for directory in mock_base_dir.iterdir()
        if directory.is_dir()
    ]
    output_files = [
        file for file in mock_base_dir.glob('**/*')
        if str(file).endswith('.csv')
    ]
    assert dirs == ['results'], (
        'Make sure the `results` directory is created in the project directory for '
        'output to result file.'
    )
    assert len(output_files) == 2, (
        'Make sure two parsed csv files are created'
    )
    assert any('pep_' in str(file) for file in output_files), (
        'Make sure the PEP list is saved to a file prefixed with `pep_`'
    )
    assert any('status_summary_' in str(file) for file in output_files), (
        'Ensure that a summary of the number of documents in each status '
        'saved to a file prefixed with `status_summary_`'
    )


@pytest.mark.skip()
def test_check_correct_output_files():
    with open(
        [file for file in output_files if 'pep' in str(file)][0], 'r',
        encoding='utf-8',
    ) as file:
        file_result = file.read()
        pep_pattern = re.compile(r'(\d)+\,PEP\s?(\d)+\s?(.)+')
        assert re.search(pep_pattern, file_result), (
            'Check the format for writing lines to `pep_`.'
            'Strings must match the view '
            '"20,PEP 20 – The Zen of Python,Active"'
        )
    with open(
        [
            file for file in output_files if 'status_summary_' in str(file)
        ][0], 'r',
        encoding='utf-8',
    ) as file:
        file_result = file.read()
        active_pattern = re.compile(r'Active,(\d)+')
        assert re.search(active_pattern, file_result), (
            'Make sure the lines in `status_summary_` '
            'are written in the correct format: `Status,Count`'
        )