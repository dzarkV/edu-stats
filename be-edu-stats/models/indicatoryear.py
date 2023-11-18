from typing import List, Optional
from models.indicatorvalue import IndicatorValue
from sqlmodel import SQLModel, Field, Relationship


class IndicatorYear(SQLModel, table=True):
    """
    Years class to table in BigQuery
    """

    __tablename__ = "anio_col"
    id_year: Optional[int] = Field(default=None, primary_key=True, index=True)
    year: int
    indicator_link: List[IndicatorValue] = Relationship(back_populates="year")
