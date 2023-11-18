from pydantic import BaseModel, ConfigDict

from schemas.indicatorvaluebase import IndicatorValueBase
from schemas.indicatoryearbase import IndicatorYearBase


class IndicatorBase(BaseModel):
    """
    Indicator's schema to reading/returning inside API
    """

    id_indicator: int
    indicator_code: str
    indicator_name: str
    # years: dict[IndicatorYearBase, IndicatorValueBase]
    model_config = ConfigDict(from_attributes=True)
