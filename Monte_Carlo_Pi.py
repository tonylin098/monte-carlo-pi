"""
@author: Tony Lin
@description: approximates the value of Pi by first having a circle
of radius r inside a square of length 2r and then randomly sampling
and counting the number of points that fall in the circle. Pi can then
be approximated by dividing the points in the circle by the total number
of points and multiplying by four.
"""

import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import random
import numpy as np


def check_in_circle(x, y):
    '''
    Checks if point is in the circle by calculating the distance from the center
    :param x: x point
    :param y: y point
    :return: true if in circle, else false
    '''

    dist = (x ** 2 + y ** 2) ** 0.5
    return dist <= 1


def random_point():
    '''
    Finds random x, y points within the dimensions
    :return: x, y points
    '''

    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    return [x, y]


def plot_accuracy(num_iter, pi_values):
    '''
    Plots the accuracy score of Pi with respect to the number of
    iterations. Accuracy score calculated as abs(estimated - true) / true
    :param num_iter: number of iterations
    :param pi_values: values of estimated Pi
    :return: The iteration with the lowest error and the respective Pi value
    '''

    fig2, ax2 = plt.subplots()
    accuracy_error = np.abs(np.array(pi_values) - np.pi) / np.pi
    ax2.plot(range(0, num_iter), accuracy_error)
    ax2.set_title("Accuracy of Pi Approximation Over Number of Iterations")
    ax2.set_xlabel("Number of Iterations")
    ax2.set_ylabel("Accuracy Error")
    fig2.canvas.draw_idle()
    plt.show()

    min_error_index = np.argmin(accuracy_error)
    return min_error_index, pi_values[min_error_index]


def estimate_pi(num_iter=1000, live_plotting=False):
    '''
    Gets num_iter amount of random points, counts how many fall within the
    circle of radius 1, and approximates Pi using:
    (number of points in circle / total number of points) * 4.0
    Option to plot the points as well as an accuracy score for each iteration
    :param num_iter: number of iterations
    :param live_plotting: option to display animated plotting
    :return: approximated value of Pi
    '''

    fig1, ax1 = plt.subplots()
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.draw()

    pi_values = []
    x, y, color = [], [], []
    num_in_circle = 0.0
    total_points = 0.0

    for i in range(0, num_iter):
        point = random_point()
        x.append(point[0])
        y.append(point[1])

        if check_in_circle(x[i], y[i]):
            num_in_circle += 1
            color.append('blue')
        else:
            color.append('red')

        total_points += 1

        pi_values.append((num_in_circle / total_points) * 4.0)

        if live_plotting:
            ax1.scatter(x[i], y[i], c=color[i])
            fig1.canvas.draw_idle()
            plt.pause(0.1)

    if not live_plotting:
        ax1.scatter(x, y, c=color)
        fig1.canvas.draw_idle()

    min_error_index, min_error_pi = plot_accuracy(num_iter, pi_values)

    return pi_values[num_iter-1], min_error_index, min_error_pi


if __name__ == "__main__":
    NUM_ITER = 100

    approx_pi, min_error_index, min_error_pi = estimate_pi(num_iter=NUM_ITER, live_plotting=True)
    print("The most accurate value of {} occurred at iteration {}".format(min_error_pi, min_error_index))
    print("The Pi value after {} iterations is {}".format(NUM_ITER, approx_pi))
