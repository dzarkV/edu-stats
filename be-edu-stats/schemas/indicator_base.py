from pydantic import BaseModel


class IndicatorBase(BaseModel):
    indicator_id: int
    indicator_name: str
    indicator_year: int
    indicator_value: float
