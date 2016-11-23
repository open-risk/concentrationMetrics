# -*- coding: utf-8 -*-
"""
Created on Fri Feb 29 14:33:17 2015
@author: openrisk
Purpose: Testing concentration metrics library
"""

import unittest
import numpy as np
import concentration_library as cl

ERROR_MARGIN = 1e-10


class TestConcentrationLib(unittest.TestCase):
    """ Test with uniform vectors of n = 0, 1, 1.000.000
    """

    def test_atkinson(self):
        vector = np.ones(1000000)
        self.assertTrue(abs(cl.atkinson(vector, 0.5) - 0.0) < ERROR_MARGIN)
        self.assertTrue(abs(cl.atkinson(vector, 1) - 0.0) < ERROR_MARGIN)
        self.assertTrue(abs(cl.atkinson(vector, 2) - 0.0) < ERROR_MARGIN)

        vector = np.zeros(1000)
        vector[0] = 1
        self.assertTrue(abs(cl.atkinson(vector, 2) - 1.0) < ERROR_MARGIN)

    def test_cl(self):
        n = 1000
        vector = np.ones(n)
        self.assertTrue(abs(cl.cr(vector, 1) - 1.0 / n) < ERROR_MARGIN)

    def test_bp(self):
        n = 1000
        vector = np.ones(n)
        self.assertTrue(abs(cl.cr(vector, 1) - cl.berger_parker(vector)) < ERROR_MARGIN)

    def test_hhi(self):
        vector = np.ones(10)
        self.assertTrue(abs(cl.hhi(vector) - 0.0) < ERROR_MARGIN)

    def test_gini(self):
        vector = np.ones(10)
        self.assertTrue(abs(cl.gini(vector) - 0.0) < ERROR_MARGIN)
        
    def test_shannon(self):
        vector = np.ones(10)
        self.assertTrue(abs(cl.shannon(vector) - 0.0) < ERROR_MARGIN)        
        
    def test_hk(self):
        n = 10
        vector = np.ones(n)
        self.assertTrue(abs(cl.hk(vector, 1) - 1.0 / n) < ERROR_MARGIN)
        self.assertTrue(abs(cl.hk(vector, 3) - 1.0 / n) < ERROR_MARGIN)

if __name__ == "__main__":

    unittest.main()

