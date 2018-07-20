from bokeh.plotting import figure
from bokeh.io import output_file, show

class BasicPlot():

    def figure_generator(self, xlab, ylab, width):
        """
        Args: xlab = label for x-axis
              ylba = label for y-axis
        Return: figure
        """
        fig = figure(x_axis_label = xlab, y_axis_label = ylab, plot_width = width)
        return fig
       
       
    def circle_values(figure, xdata, ydata):
        """
        Args:  figure = basic figure generated with figure_generator
               xdata = dataset for x axis
               ydata = dataset for y axis
        Return: circle glyph
        """
        return figure.circle(x=xdata, y=ydata)
        
        
    def viz_output(glyph, page):
        """
        Args: glyph = the generated bokeh plot
              page = html page location for visual output
        """
        output_file(page)
        show(glyph)

    
