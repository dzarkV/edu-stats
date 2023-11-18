from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from starlette import status
from starlette.exceptions import HTTPException

from data_source.bigqueryclient import get_bigquery_session
from queries.queries import indicator_by_id, whole_indicator_by_id
from models.indicator import Indicator


indicator_router = APIRouter()


@indicator_router.get(
    "/indicators/{id_indicator}",
    status_code=status.HTTP_200_OK,
    response_model=Indicator,
    response_description="Get an indicator by id from colombian education database",
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
    "/whole-indicators/{id_indicator}",
    status_code=status.HTTP_200_OK,
    response_model=list,
    response_description="Get an indicator by id with his information",
)
def get_whole_indicator_by_id(
    id_indicator: int, db: Session = Depends(get_bigquery_session), limit: int = 20
)-> list:
    """
    Get the whole indicator by id
    """
    indicator = whole_indicator_by_id(db, id_indicator, limit)
    if indicator is None:
        raise HTTPException(status_code=404, detail="Indicator not found")
    return indicator
