from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two dice of type D6
die_1 = Die(8)
die_2 = Die(8)

# Perform a certain number of die throws and put results on the list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Results analysis
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Data visualisation
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency'}
my_layout = Layout(title='Results of rolling two dice D8 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')