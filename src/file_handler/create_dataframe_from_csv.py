import pandas as pd

def create_dataframe_from_csv(csv_file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(csv_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {csv_file_path} was not found.")
