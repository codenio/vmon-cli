"""
vmon plot - plot I-Mon data

09-12-2020


codenio - Aananth K
aananthraj1995@gmail.com
"""

import click
from datetime import datetime

import numpy as np
from scipy import interpolate
import pandas as pd
import matplotlib.pyplot as plt

def get_rx_spectrum(file_name, interpolation="cubic", normalise=False):
    # Resolution of IMon 512 USB is 0.166015625 nm = 166.015 pm
    x = np.arange(1510,1595,0.166015625,dtype=float)
    dx = np.arange(1510,1595,0.001000000,dtype=float)

    # load data into data frame
    df = pd.read_csv(file_name,dtype=float,usecols=[i for i in range(3,515)],sep="\t", skiprows=2)
    # calculate mean of all the entries and reverse it
    mean = df.mean()[::-1]
    
    if interpolation == "cubic":
        # perform cublic spline interpolation
        cs = interpolate.CubicSpline(x, mean)    
        dy = cs(dx)

    if normalise:
        dy = dy /max(dy)

    return dx, dy


@click.command()
@click.argument('files', required=True ,nargs=-1)
@click.option('-p', '--path', default="./", help="path form which csv files are to be imported, default = . ")
@click.option('-t', '--title', default="I-Mon 512 USB Sprectrum", help="set custom title for the plot, default = . ")
@click.option('-n', '--normalise', is_flag=True, help="normalise the data before ploting")
@click.option('-pk', '--peaks', is_flag=True, help="show peaks in the plot")
def cli(files, path, title, normalise, peaks):
    """Plot the I-Mon data into graphs"""
    for file in files:
        plt.figure("vmon")
        plt.title(title)
        plt.xlabel("Wavelength (nm)")
        plt.ylabel("Normalised Amplitude (AU)")
        plt.grid("True")
        dx, dy = get_rx_spectrum(path+file, normalise=normalise)
        if peaks:
            dxmaxp = dx[dy.argmax()]
            plt.plot(dx,dy,label=f"{file.split('/')[0]}, {dx[dy.argmax()]:.2f} nm")
        else:
        	plt.plot(dx,dy,label="%s"%(file.split('/')[0]))
        plt.legend()
    plt.show()