from typing import Optional, Tuple

from fastapi import FastAPI, Depends, Response, Query

from .models import Record, Statistic, StatisticItem
from .memory import Data
from .depends import get_period


app = FastAPI()

data = Data()

re_sort_field = StatisticItem.get_sort_field_re()


@app.get("/statistic/", response_model=Statistic)
def show_statistic(
        period: Tuple = Depends(get_period),
        sort_by: Optional[str] = Query('date', regex=re_sort_field)
):
    return data.show(period.start, period.end, sort_by)


@app.post("/statistic/")
def add_statistic(record: Record):
    data.add(record)
    return Response(status_code=201)


@app.delete("/statistic/")
def clear_statistic():
    data.clear()
    return Response(status_code=204)
