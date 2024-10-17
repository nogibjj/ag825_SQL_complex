from extract import extract
from transform_load import load

from query import query

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/nogibjj/ag825_SQL_complex/refs/heads/main/Cancer_Data.csv?token=GHSAT0AAAAAACV7IGYD7SIT7EXG555TU4SWZYRT2SA"
    file_path = "Cancer_Data.csv"

    # Extract
    print("Extracting data...")
    extract(url, file_path)

    # Transform and load
    print("Transforming data...")
    load()

    # Query
    print("Querying data...")
    query()
