import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Creates a random walk and plot its points
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break