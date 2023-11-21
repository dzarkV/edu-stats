from typing import List, Optional
from models.indicatoryear import IndicatorValue
from sqlmodel import SQLModel, Field, Relationship


class Indicator(SQLModel, table=True):
    """
    Indicators class to table in BigQuery
    """

    __tablename__ = "indicador_col"
    id_indicator: Optional[int] = Field(default=None, primary_key=True, index=True)
    indicator_code: str
    indicator_name: str
    year_link: List[IndicatorValue] = Relationship(back_populates="indicator")
