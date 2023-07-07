import datetime
import os

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

format = '%Y-%m-%d_%H-%M-%S'
date = datetime.datetime.now().strftime(format)
filename = f'status_summary_{date}.csv'


class PepParsePipeline:
    """Additional processing of Items data."""

    def open_spider(self, spider):
        """Add a list for statuses and a total number variable."""
        self.total = 0
        self.count_list = {}

    def process_item(self, item, spider):
        """Add statuses and their number."""
        status = item['status']
        if self.count_list.get(status) is None:
            self.count_list[status] = 1
        else:
            self.count_list[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        """Save received status and quantity data to a file."""
        if not os.path.exists('results'):
            os.makedirs('results')
        with open(BASE_DIR / f'results/{filename}.csv',
                  mode='w', encoding='utf-8') as f:
            f.write('Status,Amount\n')
            for key, value in self.count_list.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{self.total}\n')
