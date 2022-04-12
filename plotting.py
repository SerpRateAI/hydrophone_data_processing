"""
Various plotting tools
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import obspy

class PrecisionDateFormatter(ticker.Formatter):
    """
    Extend the `matplotlib.ticker.Formatter` class to allow for millisecond
    precision when formatting a tick (in days since the epoch) with a
    `~datetime.datetime.strftime` format string.

    """

    def __init__(self, fmt, precision=3, tz=None):
        """
        Parameters
        ----------
        fmt : str
            `~datetime.datetime.strftime` format string.
        """
        from matplotlib.dates import num2date
        if tz is None:
            from matplotlib.dates import _get_rc_timezone
            tz = _get_rc_timezone()
        self.num2date = num2date
        self.fmt = fmt
        self.tz = tz
        self.precision = precision

    def __call__(self, x, pos=0):
        if x == 0:
            raise ValueError("DateFormatter found a value of x=0, which is "
                             "an illegal date; this usually occurs because "
                             "you have not informed the axis that it is "
                             "plotting dates, e.g., with ax.xaxis_date()")

        dt = self.num2date(x, self.tz)
        ms = dt.strftime("%f")[:self.precision]

        return dt.strftime(self.fmt).format(ms=ms)

    def set_tzinfo(self, tz):
        self.tz = tz

def plot_waveforms(obspydata, **kwargs):
    """
    obspy plotting sucks balls this is better for data explorations
    """
    data_len = len(obspydata)
    fig, ax = plt.subplots(data_len, figsize=(15, 5*data_len), sharex=True, sharey=True)
    
    # TODO : this only works for stream objects but if its already trace then it fails
    #        Make this work for trace objects
    
    if type(obspydata) == obspy.core.trace.Trace:
        obspydata = [obspydata]

    for n, tr in enumerate(obspydata):
        ax[n].plot(tr.times('matplotlib'), tr.data, **kwargs)
        ax[n].set_ylabel('Pressure (Pa)', fontsize=15)
        
    ax[n].xaxis.set_major_formatter(PrecisionDateFormatter("%H:%M:%S.{ms}"))
    
    fig.tight_layout(pad=0)
    return fig, ax

if __name__=='__main__':
    print('You on Earth have a very primitive society, you dont even make differences by the colour of ones pants!')