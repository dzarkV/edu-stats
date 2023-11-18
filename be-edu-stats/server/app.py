from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.exceptions import HTTPException

from data_source.bigqueryclient import get_bigquery_session
from models.indicator import Indicator
from schemas.indicatorbase import IndicatorBase

app = FastAPI(
    title="Query colombian education indicators",
    description="Visual query builder API",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"message": "How's it going?"}


@app.get(
    "/indicators/{id_indicator}",
    status_code=status.HTTP_200_OK,
    response_model=IndicatorBase,
)
async def get_indicator_by_id(
    id_indicator: int, db: Session = Depends(get_bigquery_session)
) -> IndicatorBase:

    if primer_indicador is None:
        raise HTTPException(status_code=404, detail="Indicator not found")
    return IndicatorBase.model_validate(primer_indicador)
