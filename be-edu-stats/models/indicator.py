from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class Indicator(Base):
    """
    Indicators class to table in BigQuery
    """
    __tablename__ = "indicador_col"
    id_indicator = Column(Integer, primary_key=True)
    indicator_code = Column(String)
    indicator_name = Column(String)
    value_relation = relationship("Value")

    def __repr__(self):
        return f"Country(id_indicator={self.id_indicator!r}, indicator_code={self.indicator_code!r}, indicator_name={self.indicator_name!r})"
