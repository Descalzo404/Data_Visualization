import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

#Defines the title of the graphic and names the axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square Value", fontsize=24)

#Defines the size of the markings on the axes
plt.tick_params(axis='both', labelsize=14)

plt.show()