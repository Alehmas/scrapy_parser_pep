import datetime

from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'

format = '%Y-%m-%d_%H-%M-%S'
date = datetime.datetime.now().strftime(format)
filename = f'status_summary_{date}.csv'


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = 0
        self.count_list = {}

    def process_item(self, item, spider):
        status = item['status']
        if status not in self.count_list:
            self.count_list[status] = 1
        else:
            self.count_list[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        with open(RESULTS_DIR / filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in self.count_list.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{self.total}\n')
