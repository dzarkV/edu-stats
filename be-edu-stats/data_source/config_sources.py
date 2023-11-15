import os

from dotenv import load_dotenv

load_dotenv()

# Google BigQuery config
big_query_uri = "/".join([os.getenv("CONN_STRING"), os.getenv("DATA_SET")])
credentials = os.getenv("CREDENTIALS")
