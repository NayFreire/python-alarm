import threading
import time

def count_to_five(name):
    for i in range(1, 6):
        print(f"{name} counts {i}")
        time.sleep(1)

# Creating Threads
thread_1 = threading.Thread(target=count_to_five, args=('Thread 1',))
thread_2 = threading.Thread(target=count_to_five, args=('Thread 2',))

# Initiating threads
thread_1.start()
thread_2.start()

# Wait for the threads to finish
thread_1.join()
thread_2.join()

print('Counting finished')