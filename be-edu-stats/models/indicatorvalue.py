from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class IndicatorValue(SQLModel, table=True):
    """
    Values class to table in BigQuery
    """

    __tablename__ = "valor_ind_col"
    id_value: Optional[int] = Field(default=None, primary_key=True)
    value: float = 0.0

    # Relations
    id_indicator: Optional[int] = Field(
        default=None, foreign_key="indicador_col.id_indicator", primary_key=True
    )
    indicator: "Indicator" = Relationship(back_populates="year_link")

    id_year: Optional[int] = Field(
        default=None, foreign_key="anio_col.id_year", primary_key=True
    )
    year: "IndicatorYear" = Relationship(back_populates="indicator_link")
