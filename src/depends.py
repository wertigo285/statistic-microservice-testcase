from datetime import date
from collections import namedtuple

from fastapi import Query
from fastapi.exceptions import HTTPException

from .models import re_date_format

Period = namedtuple('Period', ['start', 'end'])


def transform_date(param_name: str, value: str):
    try:
        value = date.fromisoformat(value)
    except Exception as ex:
        raise HTTPException(
            status_code=422, detail=f'{param_name} parameter error: {str(ex)}')
    return value


def get_period(
        start: str = Query(..., regex=re_date_format),
        end: str = Query(..., regex=re_date_format)):
    period = Period(start=transform_date('start', start),
                    end=transform_date('end', end))
    return period
