from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from schemas.indicatorvaluebase import IndicatorValueBase


class IndicatorYearBase(BaseModel):
    id_year: int
    year: int
    # value: IndicatorValueBase | None = 0
    model_config = ConfigDict(from_attributes=True)
    # value: IndicatorValueBase
