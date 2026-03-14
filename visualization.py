import matplotlib.pyplot as plt

def plot_anomalies(df):

    colors = df["anomaly"].map({1: "blue", -1: "red"})

    plt.scatter(df["requests"], df["response_time"], c=colors)

    plt.xlabel("Requests")
    plt.ylabel("Response Time")

    plt.title("Real-Time Traffic Anomaly Detection")

    plt.show()
