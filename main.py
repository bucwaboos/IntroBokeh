import numpy as np
#needed to create rows
from bokeh.layouts import row
#datareader will allow us to dl data files from other sources
import yfinance as yf
# older version import pandas_datareader as web
#adding curdoc for current function use
from bokeh.plotting import figure, show, curdoc
#show our data source
from bokeh.models import ColumnDataSource

#download stock ticker for apple from yahoo and load it into a dataframe
df = yf.download(
    "AAPL",
    start="2020-01-01",
    end="2026-10-01"
    )

df = df.reset_index()

#Flatten MultiIdnex columns
df.columns = [
    '_'.join(col).strip('_')
                        if isinstance(col, tuple)
                        else ColumnDataSource
                        for col in df.columns
]
#debug
print(df.columns)

source = ColumnDataSource(data=df)

#feed this into a line figure to show us stock data
p = figure(
    x_axis_type="datetime",
    title="Apple Stock Price"
)
p.line(x ="Date", y = "Close_AAPL", source=source)

# #changing the theme using curdoc
# curdoc().theme = "dark_minimal"

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

#scatter plot generation
#generate 50 insteances of random values chose different multiples so we have different value
#50 values multiplied by 10
# x = np.random.random(50) * 10
# #50 values multiplied by 200
# y = np.random.random(50) * 200

# #labeling x and y axis
# p = figure(title="Simple Scatter Plot",
#            x_axis_label="x", y_axis_label="y")

# #changing the size of your graphed figure
# p.width = 1280
# p.height =720

# #scatter plot with values changed post, this is how you would connect values to widgets to make plots interactive
# circle = p.circle(x, y, legend_label="Random Points ", color="yellow", size=12)
# #get glyph of the circle
# glyph = circle.glyph
# glyph.size = 200
# glyph.fill_color = "red"


# #create graphs that are side by side but move independently
# #categories 0 to 6 with a step size of 0.1
# x = np.arange(0, 6, 0.1)
# #create values using math functions sin, cos, and tan
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.tan(x)

# #figures to plot side by size
# p1 = figure()
# p1.line(x, y1)
# p2 = figure()
# p2.line(x, y2)
# p3 = figure()
# p3.line(x, y3)

# #fit all the rows to the screen
# show(row(children=[p1,p2,p3], sizing_mode="scale_width"))


# #chart bar plot
# #categories 0 to 5 with a step size of 1
# x = np.arange(0, 5, 1)
# #randomly generated values
# y = np.random.random(5) * 100

# #labeling x and y axis
# p = figure(title="Simple Bar Plot",
#            x_axis_label="x", y_axis_label="y")

# #use the p object to do the plotting with the labels for the legend
# p.vbar(x=x, top=y, width=0.5, bottom=0, color="red")


show(p)