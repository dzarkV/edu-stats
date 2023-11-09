# import os

# from google.cloud import bigquery
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session


class Client:
    """
    Client class to connect to BigQuery
    """

    # def __init__(self):
    #     os.environ[
    #         "GOOGLE_APPLICATION_CREDENTIALS"
    #     ] = "./data_source/bqprojectworldbankeducation.json"
    #
    #     self.client = bigquery.Client()

    @staticmethod
    def get_session_client():
        """Get a session client to connect to BigQuery """
        engine = create_engine(
            "bigquery://bigquery-public-data.world_bank_intl_education.international_education",
            credentials_path="./data_source/bqprojectworldbankeducation.json",
            list_tables_page_size=100,
            # connect_args={"client": self.client},
        )
        return Session(engine)

# results = engine.execute(
#     "SELECT * FROM `bigquery-public-data.world_bank_intl_education.international_education` LIMIT 100"
# ).fetchall()

# print(results)

# sql_query = """
# SELECT
#   country_name,
#   AVG(value) AS average
# FROM
#   `bigquery-public-data.world_bank_intl_education.international_education`
# GROUP BY
#     country_name
# LIMIT
#     100
# """

# query_job =client.query(sql_query)

# results = query_job.result()

# print(results.to_dataframe())
# # for row in results:
# #     print("{}: {}".format(row.country_name, row.average))
