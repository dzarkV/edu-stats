import os

from dotenv import load_dotenv

load_dotenv()

# Google BigQuery config
big_query_uri = os.getenv("CONN_STRING")
