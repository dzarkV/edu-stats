from sqlalchemy.orm import relationship

from models.base import Base
from sqlalchemy import Column, Integer


class Year(Base):
    """
    Years class to table in BigQuery
    """
    __tablename__ = "anio_col"
    id_year = Column(Integer, primary_key=True)
    year = Column(Integer)
    value_relation = relationship("Value")

    def __repr__(self):
        return f"Year(id_year={self.id_year!r}, year={self.year!r})"
