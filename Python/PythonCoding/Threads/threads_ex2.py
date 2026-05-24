import threading, time

def task(name):
    print(f"\n{name} starting")
    time.sleep(2)
    print(f"\n{name} finished")

threads = []
for i in range(1, 5):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed")