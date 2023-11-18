import os

from sqlalchemy.engine import create_engine
from sqlmodel import Session

from data_source.config_sources import big_query_uri


credentials_file = (
    f"{os.path.dirname(__file__)}/bqprojectworldbankeducation-9ad27c9d0bbf.json"
)
engine = create_engine(
    big_query_uri, credentials_path=credentials_file, list_tables_page_size=100
)


def get_bigquery_session():
    """Get a session client to connect to BigQuery"""
    try:
        db = Session(autocommit=False, autoflush=False, bind=engine, future=True)
        yield db
    finally:
        db.close()
