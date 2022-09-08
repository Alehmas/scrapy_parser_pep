BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
    # # И ещё один файл.
    # 'quotes_author.csv': {
    #     'format': 'csv',
    #     # В этот файл попадёт только список авторов.
    #     'fields': ['author'],
    #     'overwrite': True
    # },
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}