from typing import Optional

from pydantic import BaseModel, ConfigDict


class IndicatorValueBase(BaseModel):
    id_value: int
    value: float
    id_indicator: Optional[int]
    id_year: Optional[int]
    model_config = ConfigDict(from_attributes=True)
