import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square Value", fontsize=24)

plt.tick_params(axis='both', which='major', labelsize=14)


#Defines the interval of the axes
plt.axis([0, 1100, 0, 1100000])

#If you want to instead of showing the graphic saving it as a image use "plt.savefig('squares_plot.png', bbox_inches='tight')"

plt.show()