import time
from itertools import cycle

t = 1
for i in cycle([1]):
    time.sleep(.5)
    t += i
    print(t)


print('hello world')





