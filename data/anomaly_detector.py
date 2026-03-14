from sklearn.ensemble import IsolationForest

def detect_anomalies(df):

    features = df[['requests','response_time','bytes_sent']]

    model = IsolationForest(contamination=0.1, random_state=42)

    df['anomaly'] = model.fit_predict(features)

    return df
