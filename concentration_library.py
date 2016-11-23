"""
Created on Fri Nov 18 14:24:07 CET 2016
@author: openrisk
Purpose: Concentration metrics library
The library implements the computation of indexes of inequality and concentration. For
each index, it provides decomposition between subgroups. Plotting of Lorenz and concentration
curves are also available
Version: 0.2
"""
import numpy as np


# calculate total size
def total_size(vector):
    return np.sum(vector)


def get_weights(vector):
    """ Calculate the vector weights
    :param vector: Positive vector
    :return: Vector weights
    :raise: TypeError if negative total size
    """
    ts = total_size(vector)
    if ts <= 0:
        raise TypeError('Vector must be positive')
    else:
        return np.true_divide(vector, ts)


def cr(vector, n):
    """ Calculate the concentration ratio
    :param vector: Positive vector
    :param n: Integer
    :return: Concentration Ratio (Float)
    :raise: TypeError if n out of range
    """
    if n < 0 or n > vector.size:
        raise TypeError('n must be an positive integer smaller than the vector size')
    else:
        vector = sorted(vector, reverse=True)
        weights = get_weights(vector)
        return weights[:n].sum()


def berger_parker(vector):
    """ Calculate the Berger Parker index
    :param vector: Positive vector
    :return: Berger Parker (Float)
    """
    return cr(vector, 1)


def hhi(vector):
    """ Calculate the Hirschman-Herfindahl index
    :param vector: Positive vector
    :return: HHI (Float)
    """
    weights = get_weights(vector)
    n = weights.size
    if n == 0:
        return 0
    else:
        h = np.square(weights).sum()
        return (h - 1.0 / n) / (1.0 - 1.0 / n)


def hk(vector, a):
    """ Calculate the inverted Hannah Kay index
    :param vector: Positive vector
    :param a: Integer index parameter alpha
    :return: HK (Float)
    """
    weights = get_weights(vector)
    n = weights.size
    if n == 0:
        return 0
    else:
        if a <= 0:
            raise TypeError('Alpha must be strictly positive')
        elif a == 1:
            weights_nz = weights[weights != 0]
            log_weights = np.log(weights_nz)
            h = np.multiply(weights_nz, log_weights).sum()
            return np.exp(h)
        else:
            h1 = np.power(weights, a).sum()
            h2 = np.power(h1, 1.0/(a-1.0))
            return h2


def gini(vector):
    """ Calculate the Gini index
    :param vector: Positive vector
    :return: Gini (Float)
    """
    vector = sorted(vector, reverse=True)
    weights = get_weights(vector)
    n = weights.size
    if n == 0:
        return 0
    else:
        i = np.arange(1, n+1)
        return (1.0 - 2.0 * np.multiply(i, weights).sum())/n + 1.0


def shannon(vector):
    """ Calculate the Shannon entropy index
    :param vector: Positive vector
    :return: Shannon entropy (Float)
    """
    weights = get_weights(vector)
    weights_nz = weights[weights != 0]
    n = weights_nz.size
    if n == 0:
        return 0
    else:
        log_weights = np.log(weights_nz)
        h = - np.multiply(weights_nz, log_weights).sum()
        return 1.0 - h / np.log(n)


def atkinson(vector, epsilon):
    """ Calculate the Atkinson inequality index
    :param vector: Positive vector
    :param epsilon: Index parameter
    :return: Atkinson inequality (Float)
    """
    weights = get_weights(vector)
    n = weights.size
    if n == 0:
        return 0
    else:
        if epsilon < 0:
            raise TypeError('Epsilon must be strictly positive')
        elif epsilon == 1:
            weights_nz = weights[weights != 0]
            n = weights_nz.size
            log_weights = np.log(weights_nz)
            h = log_weights.sum() / n
            return 1 - n * np.exp(h)
        else:
            n2 = np.power(n, epsilon / (epsilon - 1.0))
            h1 = np.power(weights, 1.0 - epsilon).sum()
            h2 = np.power(h1, 1.0/(1.0 - epsilon))
            return 1 - n2 * h2


def gei(vector, alpha):
    """ Calculate the Generalized Entropy Index
    :param vector: Positive vector
    :param alpha: Index parameter
    :return: Generalized Entropy Index (Float)
    """
    weights = get_weights(vector)
    n = weights.size
    if n == 0:
        return 0
    else:
        if alpha == 0:
            weights_nz = weights[weights != 0]
            n = weights_nz.size
            log_weights = np.log(weights_nz)
            h = log_weights.sum() / n
            index = - (np.log(n) + h)
        elif alpha == 1:
            weights_nz = weights[weights != 0]
            n = weights_nz.size
            log_weights = np.log(weights_nz)
            h = np.multiply(weights_nz, log_weights).sum()
            index = np.log(n) + h
        else:
            n2 = np.power(n, alpha)
            h1 = n2 * np.power(weights, alpha).sum() - n
            index = h1 / n / alpha / (alpha - 1.0)
        return index


def theil(vector):
    """ Calculate the Theil Index (Generalized Entropy Index for a=1)
    :param vector: Positive vector
    :return: Theil Index (Float)
    """
    weights = get_weights(vector)
    return gei(weights, 1)


def kolm(vector, alpha):
    """ Calculate the Kolm index
    :param vector: Positive vector
    :param alpha: Index parameter
    :return: Kolm Index (Float)
    """
    n = vector.size
    if n == 0:
        return 0
    else:
        mu = vector.mean()
        weights = get_weights(vector)
        n_weights = np.multiply(- n * mu * alpha, weights)
        h = np.exp(n_weights).sum()
        return mu + (np.log(h) - np.log(n)) / alpha
