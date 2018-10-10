

# https://www.raspberrypi.org/learning/visualising-sorting-with-python/lesson-1/plan/

import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

plt.ion()



y = [i for i in range(100)]
x = [i for i in range(len(y))]

for i in range(50):
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.pause(0.0001) 
    sleep(0.5)
    shuffle(y)