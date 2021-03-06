# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:26:27 2014

@author: Nathan
"""

import numpy as np
from scipy.optimize import curve_fit

xdata = np.array([[-2,-1.64,-1.33,-0.7,0,0.45,1.2,1.64,2.32,2.9], [-2,-1.64,-1.33,-0.7,0,0.45,1.2,1.64,2.32,2.9]])
ydata = np.array([0.699369,0.700462,0.695354,1.03905,1.97389,2.41143,1.91091,0.919576,-0.730975,-1.42001])

def func(x, p1,p2):
  return p1*np.cos(p2*x[0]) + p2*np.sin(p1*x[1])

popt, pcov = curve_fit(func, xdata, ydata,p0=(1.0,0.2))

plot(transpose(xdata[0]),ydata)
plot(transpose(xdata[0]), func(xdata,popt[0], popt[1]))