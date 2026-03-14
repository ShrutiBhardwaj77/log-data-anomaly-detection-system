# Real-Time Log Analytics and Anomaly Detection System

A real-time data analytics system that simulates server log generation and applies machine learning techniques to detect anomalous system behavior.
The system continuously generates logs, performs traffic analytics, and identifies suspicious activity using an Isolation Forest anomaly detection model.

---

## Overview

Modern systems generate large volumes of log data that can contain valuable insights about system behavior and potential security threats.
This project builds a real-time analytics pipeline that processes continuously generated server logs and detects abnormal traffic patterns.

The system includes:

* Real-time log generation
* Data preprocessing and parsing
* Traffic analytics
* Machine learning based anomaly detection
* Continuous monitoring loop

---

## Key Features

* Real-time server log simulation
* Sliding window analytics for efficient processing
* Statistical traffic analysis
* Machine learning anomaly detection using Isolation Forest
* Modular and extensible architecture

---

## System Architecture

```
Log Generator
      ↓
Log Dataset (server_logs.csv)
      ↓
Log Parser
      ↓
Analytics Engine
      ↓
Isolation Forest Model
      ↓
Anomaly Detection Output
```

The pipeline continuously processes newly generated logs and updates analytics and anomaly detection results.

---

## Project Structure

```
log-data-anomaly-detection-system
│
├── main.py
├── log_generator.py
├── log_parser.py
├── anomaly_detector.py
├── analytics_engine.py
├── visualization.py
│
├── data/
│   └── server_logs.csv
│
├── models/
├── logs/
└── requirements.txt
```

---

## Components

### Log Generator

`log_generator.py`

Simulates real-time server traffic and continuously generates logs.
The generator also injects abnormal traffic spikes to simulate anomalous behavior.

Example log format:

```
timestamp,ip,requests,response_time,bytes_sent
2026-03-14 22:10:01,192.168.1.2,45,110,2100
```

---

### Log Parser

`log_parser.py`

Responsible for:

* Loading log data
* Converting timestamps to datetime
* Handling missing values
* Applying sliding window analysis (latest logs)

---

### Analytics Engine

`analytics_engine.py`

Performs statistical analysis on the logs such as:

* Average request count
* Maximum response time
* Total bytes transferred
* Top traffic generating IP addresses

---

### Anomaly Detection Model

`anomaly_detector.py`

Uses the Isolation Forest machine learning algorithm to identify abnormal traffic patterns.

Input features:

* request count
* response time
* bytes transferred

Output labels:

```
1  → Normal
-1 → Anomaly
```

---

### Main Pipeline

`main.py`

Orchestrates the system workflow:

1. Load log dataset
2. Perform traffic analytics
3. Apply anomaly detection
4. Display suspicious log entries
5. Repeat continuously

---

## Installation

Clone the repository:

```
git clone https://github.com/ShrutiBhardwaj77/log-data-anomaly-detection-system.git
```

Navigate to the project directory:

```
cd log-data-anomaly-detection-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the System

Start the log generator in one terminal:

```
python3 log_generator.py
```

Start analytics and anomaly detection in another terminal:

```
python3 main.py
```

The system will continuously generate logs and analyze them in real time.

---

##  Output

```

### Log Generator
![Log Generator](screenshots/log_generator.jpg)

### Traffic Analytics
![Analytics](screenshots/analytics_output.jpg)

### Anomaly Detection
![Anomalies](screenshots/anomaly_detection.jpg)
---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

## Applications

This system demonstrates concepts used in:

* Security log analytics
* System performance monitoring
* Network traffic analysis
* Anomaly detection in operational data

---

## Future Improvements

* Integration with streaming platforms (Kafka)
* Real-time dashboards using Kibana
* Automated alerting for detected anomalies
* Integration with security monitoring pipelines

---

## Author

Shruti Bhardwaj

GitHub: https://github.com/ShrutiBhardwaj77

