import matplotlib
import matplotlib.pyplot as plt

def init_plot_settings():
    """
    Initialize default plotting settings.
    """
    # Plot settings
    font = {'family' : 'Bitstream Vera Sans',
            'weight' : 'regular',
            'size'   : 13}
    figure = {'figsize' : (20,10)}

    matplotlib.rc('font', **font)
    matplotlib.rc('figure', **figure)
    
    plt.set_cmap("Dark2")
    plt.style.use('dark_background')