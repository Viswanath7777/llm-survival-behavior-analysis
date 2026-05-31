import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

LOG_FILE = f"logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def log(text):

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")