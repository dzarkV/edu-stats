from models.indicator import Indicator
from models.indicatorvalue import IndicatorValue
from models.indicatoryear import IndicatorYear
from queries.indicators_name import IndicatorNames
from sqlmodel import Session, select


def indicators_helper_format(results) -> list:
    """
    Helper format function to get the indicators from BigQuery

    :param results: row results from BigQuery
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


def whole_indicator_statement():
    """
    Compose the statement to get the whole indicator
    """
    return (
        select(Indicator, IndicatorYear, IndicatorValue)
        .join(IndicatorValue, Indicator.id_indicator == IndicatorValue.id_indicator)
        .join(IndicatorYear, IndicatorValue.id_year == IndicatorYear.id_year)
    )


def indicator_by_id(db: Session, ind_id: int):
    """
    Executes indicator's searching for id

    :param db: BigQuery session
    :param ind_id: indicator's id
    """
    stmt = select(Indicator).where(Indicator.id_indicator == ind_id)
    same_indicator = db.exec(stmt).first()
    if same_indicator is not None:
        return same_indicator
    return None


def whole_indicator_by_id(db: Session, ind_id: int, limit: int):
    """
    Executes compose indicator's searching for id

    :param db: BigQuery session
    :param ind_id: indicator's id
    :param limit: limit of rows to return
    """
    stmt = (
        whole_indicator_statement().where(Indicator.id_indicator == ind_id).limit(limit)
    )
    complete_indicators = db.exec(stmt).all()
    if complete_indicators is not None:
        return indicators_helper_format(complete_indicators)
    return None


def whole_indicator_by_name(db: Session, name: str, limit: int):
    """
    Executes compose indicator's searching for name

    :param db: BigQuery session
    :param name: indicator's name
    :param limit: limit of rows to return
    """
    stmt = (
        whole_indicator_statement().where(Indicator.indicator_name == name)
        .order_by(IndicatorYear.year).limit(limit)
    )
    complete_indicators = db.exec(stmt).all()
    if complete_indicators is not None:
        return indicators_helper_format(complete_indicators)
    return None


def indicators_from_enum() -> list:
    """
    Get all indicators to select from enum class
    """
    return [i.value for i in IndicatorNames]
