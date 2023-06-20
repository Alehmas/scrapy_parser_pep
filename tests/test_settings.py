from pathlib import Path

try:
    from pep_parse.settings import FEEDS, ITEM_PIPELINES
except ModuleNotFoundError as exc:
    raise AssertionError(
        'File `settings.py` not found in path '
        f'`pep_parse.{exc.name.split(".")[0]}`',
    )
except ImportError as exc:
    raise AssertionError(
        f'Settings `{exc.args[0].split()[3]}` not found in file {exc.name}',
    )


def test_settings_feeds():
    assert isinstance(FEEDS, dict), (
        'You need to declare a `FEEDS` variable in settings.py '
        'of type `dict` according to the documentation.\n'
        'Documentation link: '
        'https://docs.scrapy.org/en/latest/topics/feed-exports.html?highlight=feeds#feeds'
    )
    feeds_path = list(FEEDS.keys())
    assert len(feeds_path) == 1, (
        'In `FEEDS` only 1 key with file save path needs to be declared.'
    )
    if isinstance(feeds_path[0], Path):
        feeds_path[0] = str(feeds_path[0])
    splited_path = feeds_path[0].split('/')
    assert splited_path[0] == 'results', (
        'Make sure the `FEEDS` dictionary key precedes the filename with '
        'path to directory `results/`'
    )
    assert splited_path[1] == 'pep_%(time)s.csv', (
        'The name of the PEP listing file must be prefixed with pep_ '
        'and date substitution `%(time)s`'
    )
    path_key = list(FEEDS.keys())[0]
    fields_format_keys = FEEDS.get(path_key)
    assert fields_format_keys.get('fields') == ['number', 'name', 'status'], (
        'Make sure FEEDS has all required fields: '
        '`number, name, status`'
    )
    assert fields_format_keys.get('format') == 'csv', (
        'Check file output format in FEEDS'
    )


def test_item_pipelines():
    assert isinstance(ITEM_PIPELINES, dict), (
        'You need to declare `ITEM_PIPELINES` variable in settings.py '
        'of type `dict` according to the documentation.\n'
        'Documentation link: '
        'https://docs.scrapy.org/en/latest/topics/settings.html?highlight=ITEM_PIPELINES#item-pipelines'
    )
    item_pipelines = list(ITEM_PIPELINES.keys())
    assert len(item_pipelines) == 1, (
        'In `ITEM_PIPELINES` you need to declare 1 key with the name of the pipeline.'
    )
    assert item_pipelines[0] == 'pep_parse.pipelines.PepParsePipeline', (
        'The pipeline key in the `ITEM_PIPELINES` settings must be a class.'
    )
    assert ITEM_PIPELINES['pep_parse.pipelines.PepParsePipeline'] in range(1000), (
        'As value for key `pep_parse.pipelines.PepParsePipeline` '
        'in the settings specify a value from the range from `0` to `1000`'
    )
