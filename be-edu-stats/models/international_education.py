from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    pass


class InternationalEducation(Base):
    """
    International education class to connect to BigQuery
    """

    __tablename__ = "international_education"
    rowId = Column(Integer, primary_key=True)
    country_name: Mapped[str | None]
    country_code: Mapped[str | None]
    indicator_name: Mapped[str | None]
    indicator_code: Mapped[str | None]
    value: Mapped[float | None]
    year: Mapped[int | None]

    def __repr__(self):
        return f"<International_education(country_name={self.country_name}, country_code={self.country_code}, indicator_name={self.indicator_name}, indicator_code={self.indicator_code}, value={self.value}, year={self.year})>"
