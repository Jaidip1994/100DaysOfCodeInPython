import time
# import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} Sec(s)')
    time.sleep(seconds)
    return f'Done Sleeping for ... {seconds} Sec(s)'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # Adv of using the as_completed() method is as the threads are completed,
    # Its being returned to the main thread.
    
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    
    # Problem with the below method is that it will wait for all the threads to complete
    results = executor.map(do_something, secs)
    for res in results:
        print(res)

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for elem in threads:
#     elem.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')