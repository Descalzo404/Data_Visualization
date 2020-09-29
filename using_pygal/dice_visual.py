import pygal
from dice import Dice

#Creates a D6
dice_1 = Dice()
dice_2 = Dice(10)

#Make some rolls and keeps them in a list
results = []
for roll_num in range(5000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

#Analyzes the results
max_result = dice_1.num_sides + dice_2.num_sides
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualizes the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = [str(number) for number in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')