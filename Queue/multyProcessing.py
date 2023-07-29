from multiprocessing import Queue

customQueue = Queue(maxsize=3)
customQueue.put(5)
print(customQueue.get())