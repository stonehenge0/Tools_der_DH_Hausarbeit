import ast

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random 


# Read in data. 
with open("results\\most_frequent_tokens_results.txt", 'r') as file:
    contents = file.read()

enola_str, sherlock_str = contents.split('}{')

enola_str += '}' # Add back the closing square brackets for each list after splitting them above
sherlock_str = '{' + sherlock_str

enola = ast.literal_eval(enola_str)
sherlock = ast.literal_eval(sherlock_str)

# I think the plot looks fancier if the items aren't ordered, so we'll shuffle them around a bit
items = list(sherlock.items())
random.shuffle(items)
sherlock = dict(items)





# Actual plotting
final_dict = sherlock # Set this to the dictionary you want to have plotted

plt.figure(figsize=(20, 10)) 

# Plot polar axis.
ax = plt.subplot(111, polar=True)

plt.axis('off')

# coordinates limits
upperLimit = 100
lowerLimit = 30

max_value = max(final_dict.values())

# heights are conversion of each item value in those new coordinates
slope = (max_value - lowerLimit) / max_value
heights = [slope * value + lowerLimit for value in final_dict.values()]

# Compute the width of each bar to get to total circle
width = 2 * np.pi / len(final_dict)

indexes = list(range(1, len(final_dict) + 1))
angles = [element * width for element in indexes]

plt.figure(figsize=(20, 10))
ax = plt.subplot(111, polar=True)
plt.axis('off')

bars = ax.bar(
    x=angles,
    height=heights,
    width=width,
    bottom=lowerLimit,
    linewidth=2,
    edgecolor="white",
    color="#61a4b2",
)

labelPadding = 4


for bar, angle, height, (label, value) in zip(bars, angles, heights, final_dict.items()):
    # Labels are rotated. Rotation must be specified in degrees :(
    rotation = np.rad2deg(angle)

    # Flip some labels upside down for visibility
    alignment = ""
    if angle >= np.pi / 2 and angle < 3 * np.pi / 2:
        alignment = "right"
        rotation = rotation + 180
    else:
        alignment = "left"

    ax.text(
        x=angle,
        y=lowerLimit + bar.get_height() + labelPadding,
        s=f'{label}: {value}',
        ha=alignment,
        va='center',
        rotation=rotation,
        rotation_mode="anchor"
    )

plt.show()