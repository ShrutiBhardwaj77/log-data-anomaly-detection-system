import random
import time
import csv
from datetime import datetime

LOG_FILE = "data/server_logs.csv"

ips = [
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.9"
]

def generate_log():

    timestamp = datetime.now()
    ip = random.choice(ips)

    requests = random.randint(20, 60)
    response_time = random.randint(80, 150)
    bytes_sent = random.randint(1000, 4000)

    # simulate attack behaviour
    if random.random() < 0.05:
        requests = random.randint(400, 800)
        response_time = random.randint(500, 1000)
        bytes_sent = random.randint(10000, 20000)

    return [timestamp, ip, requests, response_time, bytes_sent]


def start_log_stream():

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        while True:

            log = generate_log()
            writer.writerow(log)

            print("Generated Log:", log)

            time.sleep(1)
if __name__ == "__main__":
    start_log_stream()
