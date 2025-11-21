from correlation import decorrelate, plot

import numpy as np
import os

def test_normal():
    rg = np.random.Generator(np.random.PCG64())

    mean = np.array([0.5, 1.5])
    covar = np.array([
        [0.81, 0.64],
        [0.64, 4.00]
    ])

    data = rg.multivariate_normal(mean, covar, 10**5)

    new_data, direct, inverse = decorrelate(data)
    new_corr = np.corrcoef(new_data[:,0], new_data[:,1])

    fname = 'scatter.png'
    if os.path.isfile(fname):
        os.remove(fname)
    plot(data, new_data)

    assert np.allclose(new_data, direct(data))
    assert np.allclose(data, inverse(new_data))
    assert np.allclose(new_data, direct(inverse(new_data)))
    assert np.allclose(new_corr, np.diag([1, 1]))
    assert os.path.isfile(fname)
