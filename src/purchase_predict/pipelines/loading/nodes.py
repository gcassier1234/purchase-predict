import pandas as pd
import glob

from google.cloud import storage


def load_csv_from_bucket(project: str, bucket_path: str) -> pd.DataFrame:
    """
    Loads multiple CSV files from bucket (as generated from Spark).
    """
    storage_client = storage.Client()
    bucket_name = bucket_path.split("/")[0]
    print(f"############ ucket ame {bucket_name}")
    folder = "/".join(bucket_path.split("/")[1:])
    print(f"############ ucket ame {folder}")
    for blob in storage_client.list_blobs(bucket_name, prefix=folder):
        filename = blob.name.split("/")[-1]
        if filename[-3:] == "csv":
            blob.download_to_filename("C:\\Users\\gcass\\AppData\\Local\\Temp\\" + filename)

    all_files = glob.glob("C:\\Users\\gcass\\AppData\\Local\\Temp\\*.csv")
    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, sep=",")
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    return df
