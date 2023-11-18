from models.indicator import Indicator
from models.indicatorvalue import IndicatorValue
from models.indicatoryear import IndicatorYear
from sqlmodel import Session, select


def indicators_helper(results)-> list:
    """
    Helper function to get the indicators from BigQuery
    """
    indicators_composed = []
    for row in results:
        indicators_composed.append(
            {   
                "indicator_id": row.Indicator.id_indicator,
                "indicator_name": row.Indicator.indicator_name,
                "indicator_year": row.IndicatorYear.year,
                "indicator_value": row.IndicatorValue.value,
            }
        )
    return indicators_composed


def indicator_by_id(db: Session, ind_id: int):
    """
    Executes indicator's searching for id from BigQuery
    """
    stmt = select(Indicator).where(Indicator.id_indicator == ind_id)
    same_indicator = db.exec(stmt).first()
    if same_indicator is not None:
        return same_indicator
    return None


def whole_indicator_by_id(db: Session, ind_id: int, limit: int):
    """
    Executes compose indicator's searching for id from BigQuery
    """
    stmt = (
        select(Indicator, IndicatorYear, IndicatorValue)
        .join(IndicatorValue, Indicator.id_indicator == IndicatorValue.id_indicator)
        .join(IndicatorYear, IndicatorValue.id_year == IndicatorYear.id_year)
        .where(Indicator.id_indicator == ind_id)
        .limit(limit)
    )
    complete_indicators = db.exec(stmt).all()
    if complete_indicators is not None:
        return indicators_helper(complete_indicators)
    return None
