from itertools import groupby
from operator import attrgetter

from .models import Statistic, StatisticItem


class Data:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Data, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.items.sort(key=lambda item: item.date)

    def clear(self):
        self.items.clear()

    def show(self, start, end, sorting_field='date'):
        period_items = filter(lambda item: start <=
                              item.date <= end, self.items)
        result = Statistic(items=[])
        for date, items in groupby(period_items, key=lambda item: item.date):
            clicks = views = cost = cpc = cpm = 0
            for item in items:
                clicks += item.clicks
                views += item.views
                cost += item.cost
            cpm = round(cost/views*1000, 2) if views else 0
            cpc = round(cost/clicks, 2) if clicks else 0
            st_it = StatisticItem(date=date, clicks=clicks,
                                  views=views, cost=cost, cpm=cpm, cpc=cpc)
            result.items.append(st_it)
            result.items.sort(key=attrgetter(sorting_field))
        return result