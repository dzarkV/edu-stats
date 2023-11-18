from sqlalchemy.orm import relationship

from data_source.bigqueryclient import Base
from sqlalchemy import Column, Integer


class IndicatorYear(Base):
    """
    Years class to table in BigQuery
    """

    __tablename__ = "anio_col"
    id_year = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    value = relationship("IndicatorValue", back_populates="years_relation")

    # def __repr__(self):
    #     return f"Year(id_year={self.id_year}, year={self.year})"

    def __repr__(self):
        return f"->{self.year}"
