import time

def funzione(id: int):
    import time
    import random

    sleep_time: int = random.randint(1, 10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")

if __name__ == "__main__":

    import threading
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(funzione, range(100))