import os
from databricks import sql
from dotenv import load_dotenv
import csv


def load():
    dataset = "Cancer_Data.csv"
    # encoding = "utf-8"

    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    # print(*payload)

    load_dotenv()
    server_h = os.getenv("DATABRICKS_SERVER_HOST_NAME")
    access_token = os.getenv("DATABRICKS_API_KEY")
    http_path = os.getenv("DATABRICKS_SERVER_HTTP")

    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """ CREATE OR REPLACE TABLE ag825_cancerDB
                           (id int,
                            diagnosis string,
                            radius_mean float,
                            texture_mean float,
                            perimeter_mean float,
                            area_mean float,
                            smoothness_mean float)
                           """
            )

            strinp = "INSERT INTO ag825_cancerDB VALUES"
            for i in payload:
                strinp += "\n" + str(tuple(i)) + ","
            strinp = strinp[:-1] + ";"

            cursor.execute(strinp)

            cursor.close()
            connection.close()


if __name__ == "__main__":
    load()
