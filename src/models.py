import re
from datetime import date
from typing import Optional, List

from pydantic import BaseModel, condecimal, PositiveInt, validator

re_date_format = r'\d{4}-\d{2}-\d{2}'


class Record(BaseModel):
    date: date
    views: Optional[PositiveInt] = 0
    clicks: Optional[PositiveInt] = 0
    cost:  Optional[condecimal(decimal_places=2)] = 0

    @validator('date', pre=True)
    def check_date_format(cls, v):
        if not re.fullmatch(re_date_format, str(v)):
            raise ValueError('Invalid date format')
        return v


class StatisticItem(BaseModel):
    date: date
    views: int
    clicks: int
    cost: condecimal(decimal_places=2)
    cpc: condecimal(decimal_places=2)
    cpm: condecimal(decimal_places=2)

    @classmethod
    def get_sort_field_re(cls):
        return r'|'.join(cls.__fields__.keys())


class Statistic(BaseModel):
    items: List[StatisticItem]
