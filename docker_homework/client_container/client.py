import requests
import time
import logging

logging.basicConfig(
    filename='client.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

time.sleep(5)

while True:
    try:
        response = requests.get('http://backend:8098/', timeout=5)
        logging.info(f"SUCCESS: Status {response.status_code} - {response.json()}")
        print(f"SUCCESS: {response.json()}")
    except Exception as e:
        logging.error(f"FAILED: {str(e)}")
        print(f"FAILED: {str(e)}")
    
    time.sleep(10)
