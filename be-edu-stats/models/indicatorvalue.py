from sqlalchemy.orm import relationship

from data_source.bigqueryclient import Base
from models.indicator import Indicator  # no qa
from models.indicatoryear import IndicatorYear  # no qa
from sqlalchemy import Column, Integer, Float, ForeignKey


class IndicatorValue(Base):
    """
    Values class to table in BigQuery
    """

    __tablename__ = "valor_ind_col"
    id_value = Column(Integer, primary_key=True, index=True)
    value = Column(Float)
    # Relations
    id_indicator = Column(
        Integer, ForeignKey("indicador_col.id_indicator"), primary_key=True
    )
    indicators_relation = relationship("Indicator", back_populates="years")
    id_year = Column(Integer, ForeignKey("anio_col.id_year"), primary_key=True)
    years_relation = relationship("IndicatorYear", back_populates="value")

    # def __repr__(self):
    #     return f"Value(id_value={self.id_value}, value={self.value}, id_indicator={self.id_indicator}, id_year={self.id_year})"
    def __repr__(self):
        return f"->{self.value}"
