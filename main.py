import numpy as np
from bokeh.plotting import figure, show

# #generate values from 0-10 with a step size of 1
# x = np.arange(0, 10, 1)
# # x squared, cubed, quartic
# y1 = x ** 2
# y2 = x ** 3
# y3 = x ** 4

# #labeling x and y axis
# p = figure(title="Simple Line Charts",
#            x_axis_label="x", y_axis_label="y")

# #use the p object to do the plotting with the labels for the legend
# p.line(x, y1, legend_label="Quadratic Function", line_width=2, color="red")
# p.line(x, y2, legend_label="Cubic Function", line_width=2, color="green")
# p.line(x, y3, legend_label="Quartic Function", line_width=2, color="blue")

# #generate 50 insteances of random values chose different multiples so we have different value
# #50 values multiplied by 10
# x = np.random.random(50) * 10
# #50 values multiplied by 200
# y = np.random.random(50) * 200

# #labeling x and y axis
# p = figure(title="Simple Scatter Plot",
#            x_axis_label="x", y_axis_label="y")

# bar plot
# p.circle(x, y, legend_label="Random Points ", color="yellow", size=12)

#chart bar plot
#categories 0 to 5 with a step size of 1
x = np.arange(0, 5, 1)
#randomly generated values
y = np.random.random(5) * 100

#labeling x and y axis
p = figure(title="Simple Bar Plot",
           x_axis_label="x", y_axis_label="y")

#use the p object to do the plotting with the labels for the legend
p.vbar(x=x, top=y, width=0.5, bottom=0, color="red")


show(p)