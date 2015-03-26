"""
Created on Fri Feb 29 14:33:17 2015
@author: openrisk
Purpose: Concentration metrics library
Version: 0.1 
"""
import numpy as np

# calculate total exposure
def exposure(portfolio):
    return np.sum(portfolio)
    
# calculate portfolio exposure weights
def weights(portfolio):
    return np.true_divide(portfolio,exposure(portfolio))

# calculate the concentration ratio
def cr(weights, n):
    return weights[:n].sum()
        
# calculate the normalized hhi concentration index
def hhi(weights):
    n = weights.size
    h = np.square(weights).sum()
    return (h - 1.0 / n) / (1.0 - 1.0 / n)
    
# calculate the inverted Hannah Kay index
def hk(weights, a):
    n = weights.size
    h1 = np.power(weights,a).sum()
    h2 = np.power(h1, 1.0/(a-1.0))
    return (h2 - 1.0 / n) / (1.0 - 1.0 / n)

# calculate the Gini index
def gini(weights):
    n = weights.size
    i = np.arange(1,n+1)
    return (1.0 - 2.0 * np.multiply(i,weights).sum())/n + 1.0

# calculate the Shannon entropy index
def shannon(weights):
    weights_nz = weights[weights!=0]
    n = weights_nz.size
    logweights = np.log(weights_nz)
    h = - np.multiply(weights_nz,logweights).sum()
    return 1.0 - h / np.log(n)

