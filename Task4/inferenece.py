import numpy as np
from sklearn import linear_model


def run_regressor(data: float) -> float:

    x = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]# house area in sq-feet
    y = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]# price in $1000s

    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    regr = linear_model.LinearRegression()

    regr.fit(x, y)

    return regr.predict(np.array(data).reshape(-1, 1))
