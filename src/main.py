from typing import Optional, Tuple, List

from fastapi import FastAPI, Depends, Response, Query

from .schemas import Record, StatisticItem
from .database import Base
from .depends import get_period


app = FastAPI()

base = Base()

re_sort_field = StatisticItem.get_sort_field_re()


@app.get("/statistic/", response_model=List[StatisticItem])
def show_statistic(
        period: Tuple = Depends(get_period),
        sort_by: Optional[str] = Query('date', regex=re_sort_field)
):
    a = base.show(period.start, period.end, sort_by)
    return a


@app.post("/statistic/")
def add_statistic(record: Record):
    base.add(record)
    return Response(status_code=201)


@app.delete("/statistic/")
def clear_statistic():
    base.clear()
    return Response(status_code=204)
