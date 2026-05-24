import threading
#New thread created
def worker():
    print("Thread is running")

t = threading.Thread(target=worker)
t.start()       #Making thread runnable

