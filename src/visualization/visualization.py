import matplotlib

def init_plot_settings():
    """
    Initialize default plotting settings.
    """
    # Plot settings
    font = {'family' : 'Bitstream Vera Sans',
                'weight' : 'regular',
                'size'   : 13}
    figure = {'figsize' : (20,8)}

    matplotlib.rc('font', **font)
    matplotlib.rc('figure', **figure)