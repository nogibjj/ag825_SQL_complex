from query import query
from extract import extract
from transform_load import load
import os
from databricks import sql
from dotenv import load_dotenv
import csv


def test_extract():
    assert extract() is not None


def test_load():
    # dataset = "Cancer_Data.csv"

    # payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # next(payload)

    # load_dotenv()
    # server_h = os.getenv("DATABRICKS_SERVER_HOST_NAME")
    # access_token = os.getenv("DATABRICKS_API_KEY")
    # http_path = os.getenv("DATABRICKS_SERVER_HTTP")

    # with sql.connect(
    #     server_hostname=server_h,
    #     http_path=http_path,
    #     access_token=access_token,
    # ) as connection:
    #     with connection.cursor() as cursor:
    #         cursor.execute("SELECT * FROM ag825_cancerdb LIMIT 10")
    #         result = cursor.fetchall()
    #         assert result is not None

    #         cursor.close()
    #         connection.close()
    assert load() == "Success"


def test_query():
    assert query() == "Success"


if __name__ == "__main__":
    test_query()
    test_load()
    test_extract()
