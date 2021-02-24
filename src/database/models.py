from sqlalchemy import Column, Integer, Date, Numeric

from .sql import Base


class Record(Base):
    __tablename__ = "records"

    id = Column('id', Integer, primary_key=True, index=True)
    date = Column('date', Date, index=True)
    views = Column('views', Integer)
    clicks = Column('clicks', Integer)
    cost = Column('cost', Numeric)
