import matplotlib.pyplot as plt
import ast
import numpy as np


with open('results\\Enola_sentiment_analysis.txt', 'r') as file:
    contents = file.read()

polarity_str, subjectivity_str = contents.split('][')

polarity_str += ']' # Add back the closing square brackets for each list after splitting them above
subjectivity_str = '[' + subjectivity_str

polarity = ast.literal_eval(polarity_str)
subjectivity = ast.literal_eval(subjectivity_str)

# Slice the list so we have a bit less slices and the graphs becomes more legible
polarity = polarity[::6]
subjectivity = subjectivity[::6]


# Generate the plot
x_values = np.arange(len(polarity))
total_elements = len(x_values)
x_values = np.array(x_values) / total_elements * 100

plt.plot(x_values, polarity, label='Polarity', color= "#D34068")

plt.plot(x_values, subjectivity, label='Subjectivity', color= "#5490FF")

# Add labels and a legend
plt.xlabel('Position relative to the whole book series in percent')
plt.ylabel('subjectivity/polarity rating')
plt.title("Enola Holmes series")

# Show the plot
plt.show()
