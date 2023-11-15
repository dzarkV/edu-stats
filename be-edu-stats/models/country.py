from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Country(Base):
    """
    Country class to table in BigQuery
    """
    __tablename__ = "pais"
    # id_country = Column(Integer, primary_key=True)
    country_code = Column(String, primary_key=True)
    country_name = Column(String)

    def __repr__(self):
        return f"Country(country_code={self.country_code}, country_name={self.country_name})"
