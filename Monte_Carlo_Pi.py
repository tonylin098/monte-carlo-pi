"""
@author: Tony Lin
@description: approximates the value of Pi by first having a circle
of radius r inside a square of length 2r and then randomly sampling
(Monte Carlo) and counting the number of points that fall in the circle.
Pi can then be approximated by dividing the points in the circle by the
total number of points and multiplying by four.
"""

import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import math
import random

fig, ax = plt.subplots()

pi = []
color = 'blue'
num_iter = 100
num_in_circ = 0.0
num_in_sq = float(num_iter)

plt.xlim(-1, 1)
plt.ylim(-1, 1)

plt.draw()

for i in range(0, num_iter):
    x = random.randrange(-10000, 10000)/10000
    y = random.randrange(-10000, 10000)/10000

    dist = math.hypot(x, y)
    if dist <= 1:
        num_in_circ += 1
        color = 'blue'
    else:
        color = 'red'

    ax.scatter(x, y, c=color)
    fig.canvas.draw_idle()
    plt.pause(0.01)

    pi.append((num_in_circ/num_in_sq)*4.0)

print(pi[num_iter-1])
plt.waitforbuttonpress()
