"""This is a simple program to test a random walk without using loops.

a person rolls a special dice with numbers -2,2,-3 and 3 representing neative and positive steps,
in horizontal and vertical directions respectively."""

import numpy as np
import matplotlib.pyplot as plt





# Generating random dice outcomes in an array (15 rollos of dice for this case) :

random_choice = np.int_(np.random.choice([-3, 3, 2, -2], size=(1,25)))

# x is the horizontal moves created by the dice:

# x_positive keeps track to walker x location only when the positive outcme of dice happens
# x_negative keeps track to walker x location only when the negative outcme of dice happens

x_positive = np.cumsum(random_choice == 2) 
x_negative = np.cumsum(random_choice == -2)

x_location = x_positive - x_negative    # keeps track of walker horizontal location


# y is the horizontal moves created by the dice:
# y_positive keeps track to walker x location only when the positive outcme of dice happens
# y_negative keeps track to walker x location only when the negative outcme of dice happens

y_positive = np.cumsum(random_choice == 3)

y_nagative = np.cumsum(random_choice == -3)

y_location = y_positive - y_nagative    # keeps track of walker vertical location


# Zeroth step, an array with only 0 value is created and concatenated to x and y location array to represnt the starting point
zero_point = np.array([0])

# horizontal & Vertical location based on random choice outcomes starting at (0,0)

x_array = np.concatenate((zero_point, x_location))
y_array = np.concatenate((zero_point, y_location))

# Here the seperated x and y locations are put together for each step

step_location=zip(x_array,y_array)

# converted to list to plot the (x,y) pairs

list_steps= list(step_location)

start =plt.scatter(list_steps[0][0],list_steps[0][1], s = 200, label = "Start")
end = plt.scatter(list_steps[-1][0],list_steps[-1][1], color = "r", s=150, label = "End" )
lines =plt.plot(*zip(*list_steps), color = "pink")
plt.legend(loc = "best")
plt.show()
