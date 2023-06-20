import inspect

import scrapy

try:
    from pep_parse.items import PepParseItem
except ModuleNotFoundError:
    raise AssertionError('File `items.py` not found')
except ImportError as exc:
    raise AssertionError(f'Class `PepParseItem` not found in file {exc.name}')


def test_items_fields():
    assert inspect.isclass(PepParseItem), (
        '`PepParseItem` must be a class.'
    )
    assert issubclass(PepParseItem, scrapy.Item), (
        '`PepParseItem` must inherit from `scrapy.Item`'
    )
    fields = ['number', 'name', 'status']
    for field in fields:
        assert field in list(PepParseItem.fields.keys()), (
            f'Attribute `{field}` is missing in `PepParseItem`'
        )
