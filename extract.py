import requests


def extract(
    url="https://raw.githubusercontent.com/nogibjj/ag825_sqlite_lab/refs/heads/main/Cancer_Data.csv",
    file_path="Cancer_Data.csv",
):
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        with requests.get(url, timeout=10) as r:
            with open(file_path, "wb") as f:
                f.write(r.content)
                print("YES")
    return file_path


if __name__ == "__main__":
    extract()
