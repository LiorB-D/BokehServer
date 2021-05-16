from bokeh.plotting import figure
from bokeh.io import curdoc

x = [1,2,3,4,5]
y = [4,6,2,4,3]

p = figure(
    title='Simple Graph',
    x_axis_label="X Axis",
    y_axis_label="Y Axis"
)

p.line(x, y, line_width=2)

curdoc().title = "Hello, world!"
curdoc().add_root(p)