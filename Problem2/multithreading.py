import threading
import time

def thread_function(thread_number, stop_event):
    start_time = time.time()
    while not stop_event.is_set():
        elapsed_time = int(time.time() - start_time)
        print(f"Thread {thread_number} is running at {elapsed_time}")
        time.sleep(5)

def manage_threads():
    stop_event1 = threading.Event()
    stop_event2 = threading.Event()
    stop_event3 = threading.Event()
    
    thread1 = threading.Thread(target=thread_function, args=(1, stop_event1))
    thread3 = threading.Thread(target=thread_function, args=(3, stop_event3))
    
    thread1.start()
    thread3.start()
    
    time.sleep(20)
    
    stop_event1.set()
    thread1.join()
    
    thread2 = threading.Thread(target=thread_function, args=(2, stop_event2))
    thread2.start()
    
    time.sleep(18)
    
    stop_event3.set()
    thread3.join()
    
    stop_event1.clear()
    thread1 = threading.Thread(target=thread_function, args=(1, stop_event1))
    thread1.start()
    
    time.sleep(18)
    
    stop_event2.set()
    thread2.join()
    
    stop_event1.set()
    thread1.join()

if __name__ == "__main__":
    manage_threads()
