from log_parser import load_logs
from anomaly_detector import detect_anomalies
from analytics_engine import analyze_logs
import time


def main():

    while True:

        df = load_logs("data/server_logs.csv")

        df = detect_anomalies(df)

        analyze_logs(df)

        print("\nDetected Anomalies:\n")
        print(df[df["anomaly"] == -1])

        time.sleep(5)


if __name__ == "__main__":
    main()
