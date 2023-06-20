import inspect

import scrapy

try:
    from pep_parse.spiders.pep import PepSpider
except ModuleNotFoundError:
    raise AssertionError('File `pep.py` not found')
except ImportError as exc:
    raise AssertionError(
        f'Class `{exc.args[0].split()[3]}` not found in file {exc.name}',
    )


def test_pep_spider():
    assert inspect.isclass(PepSpider), (
        '`PepSpider` must be a class.'
    )
    assert issubclass(PepSpider, scrapy.Spider), (
        '`PepSpider` must inherit from `scrapy.Spider`'
    )


def test_pep_spider_attrs():
    assert PepSpider.name, (
        'The `PepSpider` class must have a `name` attribute.'
    )
    assert PepSpider.name == 'pep', (
        'The value of the `name` attribute of the `PepSpider` class is best set to `pep`'
    )
    assert hasattr(PepSpider, 'start_urls'), (
        'The `PepSpider` class must have a `start_urls` attribute.'
    )
    assert PepSpider.start_urls == ['https://peps.python.org/'], (
        'In the PepSpider class, set the start_urls attribute to a list with the value '
        'https://peps.python.org/'
    )


def test_pep_spider_parse():
    got = PepSpider()
    assert hasattr(got, 'parse'), (
        f'Class `{got.__class__.__name__}` must have a `parse` method.'
    )
    assert callable(got.parse), (
        f'Make sure `parse` in class {got.__class__.__name__}'
        'is the method to be called.'
    )


def test_pep_spider_parse_pep():
    got = PepSpider()
    assert hasattr(got, 'parse_pep'), (
        f'The class `{got.__class__.__name__}` must have a method `parse_pep`.'
    )
    assert callable(got.parse_pep), (
        f'Make sure `parse_pep` is in class {got.__class__.__name__} '
        'is the method to be called.'
    )
