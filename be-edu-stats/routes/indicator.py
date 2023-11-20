from schemas.indicator_base import IndicatorBase
from queries.indicators_name import IndicatorNames
from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette import status
from starlette.exceptions import HTTPException

from data_source.bigqueryclient import get_bigquery_session
from queries.queries import (
    indicator_by_id,
    whole_indicator_by_id,
    whole_indicator_by_name,
    indicators_from_enum
)
from models.indicator import Indicator


indicator_router = APIRouter()


@indicator_router.get(
    "/indicators-single/{id_indicator}",
    status_code=status.HTTP_200_OK,
    description="Get a single indicator by id from colombian education database",
    response_model=Indicator,
    response_description="Indicator id, name and code",
)
def get_indicator_by_id(
    id_indicator: int, db: Session = Depends(get_bigquery_session)
) -> Indicator:
    """
    Get an indicator by id
    """
    indicator = indicator_by_id(db, id_indicator)
    if indicator is None:
        raise HTTPException(status_code=404, detail="Indicator not found")
    return indicator


@indicator_router.get(
    "/indicators/{id_indicator}",
    status_code=status.HTTP_200_OK,
    description="Get one indicator by id with its values",
    response_model=list[IndicatorBase],
    response_description="Indicator with his values-year based",
)
def get_whole_indicator_by_id(
    id_indicator: int, db: Session = Depends(get_bigquery_session), limit: int = 20
) -> list[IndicatorBase]:
    """
    Get the whole indicator by id
    """
    indicator = whole_indicator_by_id(db, id_indicator, limit)
    if indicator is None:
        raise HTTPException(status_code=404, detail="Indicator not found")
    return indicator


@indicator_router.get(
    "/indicators",
    status_code=status.HTTP_200_OK,
    description="Get one indicator by some selected names with its values",
    response_model=list[IndicatorBase],
    response_description="Indicator with his values-year based",
)
def get_whole_indicator_by_name(
    indicator_name: IndicatorNames,
    db: Session = Depends(get_bigquery_session),
    limit: int = 20,
) -> list[IndicatorBase]:
    """
    Get the whole indicator by name
    """
    indicator = whole_indicator_by_name(db, indicator_name, limit)
    if indicator is None:
        raise HTTPException(status_code=404, detail="Indicator not found")
    return indicator


@indicator_router.get(
    "/indicators-to-select",
    status_code=status.HTTP_200_OK,
    description="Get all indicators to select from a single select list",
    response_model=list[str],
    response_description="Id, name, year and value's indicator to select",
)
def get_indicatorse_name_to_select()-> list[str]:
    """
    Get all indicators to select from single select list
    """
    return indicators_from_enum() if indicators_from_enum() is not [] else HTTPException(status_code=404, detail="No indicators to select")


@indicator_router.post(
    "/indicators/{indicator_name}",
    status_code=status.HTTP_200_OK,
    description="Post an indicator by name with comments",
    response_model=IndicatorBase,
    response_description="Save an indicator with his values"
)
def post_indicator_by_name(
    indicator_name: IndicatorNames,
    db: Session = Depends(get_bigquery_session),
) -> IndicatorBase:
    """
    Post an indicator by name
    """
    return {"message": "Indicator (not yet) saved"}