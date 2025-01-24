# MULTIPROCESSING IN PYTHON

import concurrent.futures
import requests
from multiprocessing import Pool

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"
# pros = []
# for i in range(50):
#   # downloadFile(url, i)
#   p = multiprocessing.Process(target=downloadFile, args=[url, i])
#   p.start()
#   pros.append(p)

# for p in pros:
#   p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results: 
    print(r)




def process_task(task):
    # Do some work here
    print("Task processed:", task)

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)



def producer(queue):
    for i in range(10):
        queue.put(i)


def consumer(queue):
    while True:
        item = queue.get()
        print(item)


# queue = multiprocessing.Queue()
# p1 = multiprocessing.Process(target=producer, args=(queue,))
# p2 = multiprocessing.Process(target=consumer, args=(queue,))
# p1.start()
# p2.start()



# def increment(counter, lock):
#     for i in range(10000):
#         lock.acquire()
#         counter.value += 1
#         lock.release()

# if __name__ == '__main__':
#     counter = multiprocessing.Value('i', 0)
#     lock = multiprocessing.Lock()

#     p1 = multiprocessing.Process(target=increment, args=(counter, lock))
#     p2 = multiprocessing.Process(target=increment, args=(counter, lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("Counter value:", counter.value)