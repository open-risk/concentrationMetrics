# encoding: utf-8

# (c) 2017-2018 Open Risk, all rights reserved
#
# Concentration Library is licensed under the MIT license a copy of which is included
# in the source distribution of TransitionMatrix. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.


""" Concentration Library

.. moduleauthor: Open Risk

"""

import numpy as np


# TODO Enhance API: calculate weights by default


# ADJUST THIS TO REFLECT YOUR OWN ENVIRONMENT!
# Set the full path including trailing slash
source_path = '/path_to_concentration_library/'


# calculate total size
def total_size(vector):
    return np.sum(vector)


def get_weights(vector):
    """ Calculate the vector weights

    :param vector: Positive vector of weights
    :type vector: numpy array
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
    :type vector: numpy array
    :param n: Integer selecting the top-n entries
    :type n: int
    :return: Concentration Ratio (Float)
    :raise: TypeError if n out of range

    `Open Risk Manual Entry for Concentration Ratio <http://www.openriskmanual.org/wiki/Concentration_Ratio>`_
    """
    if n < 0 or n > vector.size:
        raise TypeError('n must be an positive integer smaller than the vector size')
    else:
        vector = sorted(vector, reverse=True)
        weights = get_weights(vector)
        return weights[:n].sum()


def berger_parker(vector):
    """ Calculate the Berger Parker index (special version of the Concentration Ratio)

    :param vector: Positive vector
    :type vector: numpy array
    :return: Berger Parker (Float)

    `Open Risk Manual Entry for Berger-Parker Index <http://www.openriskmanual.org/wiki/Concentration_Ratio>`_
    """
    return cr(vector, 1)


def hhi(vector):
    """ Calculate the Hirschman-Herfindahl index

    :param vector: Positive vector
    :type vector: numpy array
    :return: HHI (Float)

    `Open Risk Manual Entry for Hirschman-Herfindahl index <http://www.openriskmanual.org/wiki/Herfindahl-Hirschman_Index>`_
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
    :type vector: numpy array
    :param a: Integer index parameter alpha
    :return: HK (Float)

    `Open Risk Manual Entry for Hannah Kay Index <http://www.openriskmanual.org/wiki/Hannah_Kay_Index>`_
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
    :type vector: numpy array
    :return: Gini (Float)

    `Open Risk Manual Entry for Gini Index <http://www.openriskmanual.org/wiki/Gini_Index>`_
    """
    vector = sorted(vector, reverse=True)
    weights = get_weights(vector)
    n = weights.size
    if n == 0:
        return 0
    else:
        i = np.arange(1, n+1)
        return 1.0 + (1.0 - 2.0 * np.multiply(i, weights).sum())/n


def shannon(vector):
    """ Calculate the Shannon entropy index

    :param vector: Positive vector
    :type vector: numpy array
    :return: Shannon entropy (Float)

    `Open Risk Manual Entry for Shannon entropy index <http://www.openriskmanual.org/wiki/Shannon_Index>`_
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
    :type vector: numpy array
    :param epsilon: Index parameter
    :type epsilon: float
    :return: Atkinson inequality (Float)

    .. Todo :: Resolve divide by zero when N is very large

    `Open Risk Manual Entry for Atkinson Index <http://www.openriskmanual.org/wiki/Atkinson_Index>`_
    """
    weights = get_weights(vector)
    n = weights.size
    if n == 0:
        return 0
    else:
        if epsilon <= 0:
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
    :type vector: numpy array
    :param alpha: Index parameter
    :return: Generalized Entropy Index (Float)

    `Open Risk Manual Entry for Generalized Entropy Index <http://www.openriskmanual.org/wiki/Generalized_Entropy_Index>`_
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
    :type vector: numpy array
    :return: Theil Index (Float)

    `Open Risk Manual Entry for Theil Index <http://www.openriskmanual.org/wiki/Theil_Index>`_
    """
    weights = get_weights(vector)
    return gei(weights, 1)


def kolm(vector, alpha):
    """ Calculate the Kolm index

    :param vector: Positive vector
    :type vector: numpy array
    :param alpha: Index parameter
    :return: Kolm Index (Float)

    `Open Risk Manual Entry for Kolm Index <http://www.openriskmanual.org/wiki/Kolm_Index>`_
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
