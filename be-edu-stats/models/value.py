from models.base import Base
from sqlalchemy import Column, Integer, Float, ForeignKey


class Value(Base):
    """
    Values class to table in BigQuery
    """
    __tablename__ = "valor_ind_col"
    id_value = Column(Integer, primary_key=True)
    value = Column(Float)
    id_indicator = Column(Integer, ForeignKey("indicador_col.id_indicator"))
    id_year = Column(Integer, ForeignKey("anio_col.id_year"))

    def __repr__(self):
        return f"Value(id_value={self.id_value!r}, value={self.value!r}, id_indicator={self.id_indicator!r}, id_year={self.id_year!r})"
