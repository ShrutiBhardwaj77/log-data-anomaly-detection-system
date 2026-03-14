from log_parser import load_logs
from anomaly_detector import detect_anomalies

def main():

    df = load_logs("data/server_logs.csv")

    df = detect_anomalies(df)

    print("\nDetected anomalies:\n")

    print(df[df['anomaly'] == -1])

if __name__ == "__main__":
    main()
