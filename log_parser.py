import pandas as pd

def load_logs(file_path):
    df = pd.read_csv(file_path)

    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed')

    df.fillna(0, inplace=True)

    return df
