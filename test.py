# -*- coding: utf-8 -*-
"""
Created on Fri Feb 29 14:33:17 2015
@author: openrisk
Purpose: Testing concentration metrics library
"""

import unittest
import numpy as np
import concentration_library as cl

ERROR_MARGIN = 1e-15

class TestConcentrationLib(unittest.TestCase):
    
    # all tests uniform portfolio of 10 exposures

    def test_cl(self):
        portfolio = np.ones(10)
        portfolio = sorted(portfolio, reverse=True)
        weights = cl.weights(portfolio)
        self.assertTrue(abs(cl.cr(weights,1) - 0.1) < ERROR_MARGIN)

    def test_hhi(self):
        portfolio = np.ones(10)
        portfolio = sorted(portfolio, reverse=True)
        weights = cl.weights(portfolio)
        self.assertTrue(abs(cl.hhi(weights) - 0.0) < ERROR_MARGIN)

    def test_gini(self):
        portfolio = np.ones(10)
        portfolio = sorted(portfolio, reverse=True)
        weights = cl.weights(portfolio)
        self.assertTrue(abs(cl.gini(weights) - 0.0) < ERROR_MARGIN)
        
    def test_shannon(self):
        portfolio = np.ones(10)
        portfolio = sorted(portfolio, reverse=True)
        weights = cl.weights(portfolio)
        self.assertTrue(abs(cl.shannon(weights) - 0.0) < ERROR_MARGIN)        
        
    def test_hk(self):
        portfolio = np.ones(10)
        portfolio = sorted(portfolio, reverse=True)
        weights = cl.weights(portfolio)
        self.assertTrue(abs(cl.hk(weights,3) - 0.0) < ERROR_MARGIN)              

if __name__ == "__main__":

    unittest.main()

