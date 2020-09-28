from random import choice

class RandomWalk():
    """A class to generate random walks"""

    def __init__(self, numpoints=5000):
        """Initialize the atributtes of a random walk"""
        self.num_points = numpoints

        #Every walk starts in the (0,0) position
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculates every point of the walk"""

        #Continues to walk until the walk reach the desired size
        while len(self.x_values) < self.num_points:

            #Decides wich direction to go and the distance of every step
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #Rejects the steps that move nowhere
            if x_step == 0 and y_step == 0:
                continue
        
            #Calculates the next values of x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)