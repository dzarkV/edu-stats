from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data_source.bigqueryclient import Base


class Indicator(Base):
    """
    Indicators class to table in BigQuery
    """

    __tablename__ = "indicador_col"
    id_indicator = Column(Integer, primary_key=True, index=True)
    indicator_code = Column(String)
    indicator_name = Column(String)
    years = relationship("IndicatorValue", back_populates="indicators_relation")

    # def __repr__(self):
    #     return f"Indicator(id_indicator={self.id_indicator}, indicator_code={self.indicator_code}, indicator_name={self.indicator_name})"
