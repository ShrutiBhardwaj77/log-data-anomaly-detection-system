import pandas as pd

def analyze_logs(df):

    print("\nTraffic Analytics")

    print("Average Requests:", df["requests"].mean())

    print("Max Response Time:", df["response_time"].max())

    print("Total Bytes Sent:", df["bytes_sent"].sum())

    print("\nTop IP Traffic:")

    print(df.groupby("ip")["requests"].sum().sort_values(ascending=False))
