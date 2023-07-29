from collections import deque


customQueue = deque(maxlen= 3)
print(customQueue)

customQueue.append(2)
customQueue.append(4)
customQueue.popleft()
print(customQueue)

