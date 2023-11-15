import os

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

from data_source.config_sources import big_query_uri, credentials


def get_session_client():
    """Get a session client to connect to BigQuery """

    engine = create_engine(
        big_query_uri,
        credentials_path=f"{os.path.dirname(__file__)}/{credentials}.json",
        list_tables_page_size=100,
    )
    with Session(engine, future=True) as session:
        return session
