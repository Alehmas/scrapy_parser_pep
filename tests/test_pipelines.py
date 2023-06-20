import inspect

try:
    from pep_parse.pipelines import PepParsePipeline
except ModuleNotFoundError as exc:
    raise AssertionError(
        'File `pipelines.py` not found in path '
        f'`pep_parse.{exc.name.split(".")[0]}`',
    )
except ImportError as exc:
    raise AssertionError(
       f'Class `PepParsePipeline` not found in file {exc.name}',
    )


def test_pep_parse_pipeline():
    assert inspect.isclass(PepParsePipeline), (
        '`PepParsePipeline` must be a class.'
    )


def test_pipeline_open_spider():
    got = PepParsePipeline()
    assert hasattr(got, 'open_spider'), (
        f'The class `{got.__class__.__name__}` must have an `open_spider` method.'
    )
    assert callable(got.open_spider), (
        f'`open_spider` of class {got.__class__.__name__} must '
        'be a callable method.'
    )
    pep_pipeline_signature = list(
        inspect.signature(got.open_spider).parameters,
    )
    assert pep_pipeline_signature == ['spider'], (
        f'The `open_spider` method of class {got.__class__.__name__} must '
        'accept `spider` parameter'
    )


def test_pipeline_process_item():
    got = PepParsePipeline()
    assert hasattr(got, 'process_item'), (
        f'In class `{got.__class__.__name__}` '
        'there must be a `process_item` method.'
    )
    assert callable(got.process_item), (
        f'`process_item` of class {got.__class__.__name__} must '
        'be a callable method.'
    )
    pep_parse_pipeline_signature = list(
        inspect.signature(got.process_item).parameters,
    )
    assert pep_parse_pipeline_signature == ['item', 'spider'], (
        f'The `process_item` method of class {got.__class__.__name__} must '
        'accept parameters `item, spider`'
    )


def test_pipeline_close_spider():
    got = PepParsePipeline()
    assert hasattr(got, 'close_spider'), (
        f'In class `{got.__class__.__name__}` '
        'there must be a `close_spider` method.'
    )
    assert callable(got.close_spider), (
        f'`close_spider` of class {got.__class__.__name__} must '
        'be a callable method.'
    )
    pep_parse_pipeline_signature = list(
        inspect.signature(got.close_spider).parameters,
    )
    assert pep_parse_pipeline_signature == ['spider'], (
        f'The `close_spider` method of class {got.__class__.__name__} must '
        'accept `spider` parameter'
    )
