#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:52:06 2018

@author: Tony Lin
"""
import math
import random
import matplotlib.pyplot as plt

def approx_pi(num_iter = 10000, range_start = -1, range_end = 1):
    x = []
    y = []
    circ_sq = []
    num_circ = 0.0
    num_sq = float(num_iter)
    for i in range(0, num_iter):
        x.append(random.randrange(-10000, 10000)/10000)
        y.append(random.randrange(-10000, 10000)/10000)
        dist = math.hypot(x[i], y[i])
        if dist <= 1:
            num_circ = num_circ + 1
            circ_sq.append(1)
        else:
            circ_sq.append(0)
    pi = (num_circ/num_sq)*4.0
    return pi, x, y, circ_sq

pi, x, y, circ_sq = approx_pi(num_iter = 100_000)

fig = plt.figure()
plt.axis('equal')
plt.scatter(x, y, c = circ_sq)
print(pi)