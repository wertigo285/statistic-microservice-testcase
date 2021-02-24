from sqlalchemy import func, Numeric
from sqlalchemy.sql.functions import coalesce

from . import models
from ..schemas import Record
from .sql import SessionLocal


class Base:

    def __init__(self):
        self._session = SessionLocal()

    def add(self, record: Record):
        db_record = models.Record(
            date=record.date, views=record.views,
            clicks=record.clicks, cost=record.cost
        )
        self._session.add(db_record)
        self._session.commit()

    def clear(self):
        self._session.query(models.Record).delete()
        self._session.commit()

    def show(self, start, end, sorting_field='date'):
        return self._session.query(models.Record.date.label('date'),
                                   func.sum(models.Record.clicks).label('clicks'),
                                   func.sum(models.Record.views).label('views'),
                                   func.cast(func.sum(models.Record.cost),
                                             Numeric(10, 2)).label('cost'),
                                   func.cast(coalesce(func.sum(models.Record.cost) /
                                                      func.sum(models.Record.views) *
                                                      1000, 0),
                                             Numeric(10, 2)).label('cpm'),
                                   func.cast(coalesce(func.sum(models.Record.cost) /
                                                      func.sum(models.Record.clicks), 0),
                                             Numeric(10, 2)).label('cpc'),
                                   ).group_by(models.Record.date
                                              ).order_by(sorting_field
                                                         ).all()
