from bokeh.plotting import figure
from bokeh.io import output_file, show


#Class to create a basic Bokeh plot, allows user to overlay a second set of data
class BasicPlot():

    
    #Creates a basic figure, specify an x-axis label, y-axis label and figure width
    def figure_generator(self, xlab, ylab, width):
        """
        Args: xlab = label for x-axis
              ylba = label for y-axis
        Return: figure
        """
        fig = figure(x_axis_label = xlab, y_axis_label = ylab, plot_width = width)
        return fig
       
        
    #Creates a set of circle values to populate the figure, and x/y data sets to be plotted   
    def circle_values(figure, xdata, ydata):
        """
        Args:  figure = basic figure generated with figure_generator
               xdata = dataset for x axis
               ydata = dataset for y axis
        Return: circle glyph
        """
        return figure.circle(x=xdata, y=ydata)
    
    
    #Creates a set of x values to be populated as an overlay with the circle points, passed new x and y data sets
    def x_values(figure, xdata, ydata):
        """
        Args:  figure = basic figure generated with figure_generator
               xdata = dataset for x axis
               ydata = dataset for y axis
        Return: x glyph overlayed onto circle glyph figure
        """
        return figure.circle(x=xdata, y=ydata)
        
        
    #Generates the visual output, pass the created figure glyph, and the output html location    
    def viz_output(glyph, page):
        """
        Args: glyph = the generated bokeh plot
              page = html page location for visual output
        """
        output_file(page)
        show(glyph)

    
