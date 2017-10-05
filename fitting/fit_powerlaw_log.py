from scipy import optimize

powerlaw = lambda x, amp, index: amp * (x**index)


fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

def fit_powerlaw(data, emin=1e2, emax=1e6, pinit = [1.0, -1.0]):
    """
    Function used for spectral fitting.
    Fit a powerlaw on the loglog of y(x)
    data : list of three arrays [x,y,y_err]
    """

    xdata = data[0]
    ydata = data[1]
    yerr = data[2]
    mask = (xdata>emin) & (xdata<emax)
    logx = np.log10(xdata[mask])
    logy = np.log10(np.abs(ydata)[mask])
    logyerr = yerr[mask]/ydata[mask]
    out = optimize.leastsq(errfunc, pinit,
                       args=(logx, logy, logyerr), full_output=1)
    return out



xdata = data[0]
ydata = data[1]
yerr = data[2]

out = fit_powerlaw(data, emin=2e3, emax=10e3)

pfinal = out[0]
covar = out[1]
index = pfinal[1]
amp = 10.0**pfinal[0]



plt.loglog(xdata, powerlaw(xdata, amp, index))
plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
plt.xlabel('X (log scale)')
plt.ylabel('Y (log scale)')
plt.axis([1e2,1e5,1e-20,1e-14])
plt.show()
