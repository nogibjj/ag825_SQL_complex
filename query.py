import os
from databricks import sql
from dotenv import load_dotenv


def query():

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
                """ 
                SELECT diameter_catg AS Diameter_Category, COUNT(DISTINCT id) AS Number_of_records
                FROM
                (
                    SELECT DISTINCT *, 
                    CASE WHEN diameter_mean>=29 
                    THEN "Above Average" 
                    ELSE "Below Average" 
                    END AS diameter_catg
                    FROM
                    (
                        SELECT DISTINCT a.*, b.diameter_mean
                        FROM ag825_cancerDB a
                        LEFT JOIN
                        (
                            SELECT DISTINCT id, radius_mean*2 AS diameter_mean
                            FROM ag825_cancerDB
                        ) b
                        ON a.id=b.id
                    )
                )
                GROUP BY diameter_catg
                ORDER BY diameter_catg
                """
            )

            print("Diameter characteristics have been detailed below")
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
            connection.close()

    return "Success"


if __name__ == "__main__":
    query()
