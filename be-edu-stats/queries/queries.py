from sqlalchemy.orm import Session

from data_source.bigqueryclient import get_bigquery_session
from sqlalchemy import select

from models.indicator import Indicator
from models.indicatorvalue import IndicatorValue

session = get_bigquery_session()

stmt_country = (
    select(IndicatorValue.value, Indicator.indicator_name)
    .where(
        Indicator.indicator_name.contains(
            "Percentage of teachers in lower secondary education"
        )
    )
    .join(Indicator, IndicatorValue.id_indicator == Indicator.id_indicator)
    .limit(200)
)
results = session.execute(stmt_country).all()

if results.__len__() > 0:
    print(results.__len__())
    for row in results:
        print(row.)
else:
    print("No rows")


def indicators_pr_sc_by_id(db: Session, ind_id: int):
    primer_indicador = db.query(Indicator).filter_by(id_indicator=ind_id).first()

