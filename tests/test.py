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

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 29 14:33:17 2015
@author: Open Risk
Purpose: Testing concentration metrics library

"""

import unittest

import numpy as np
import pandas as pd

import concentration_library as cl

ERROR_MARGIN = 1e-10


class TestConcentrationLib(unittest.TestCase):
    """ Testing all indexes with uniform vectors of n = 0, 1, 1.000.000

    """

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc

    def test_compare_atkinson_with_R(self):
        """ Atkinson Index: Comparison with R version in ineq package

        Results
        Atkinson a=0.5:   0.1796591
        Atkinson a=1:     0.3518251
        """
        myIndex = cl.Index()
        x = np.array([541, 1463, 2445, 3438, 4437, 5401, 6392, 8304, 11904, 22261])
        ERROR_MARGIN = 1e-5
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.atkinson(x, 0.5) - 0.1796591) < ERROR_MARGIN)
        self.assertTrue(abs(myIndex.atkinson(x, 1.0) - 0.3518251) < ERROR_MARGIN)

    def test_atkinson_uniform(self):
        myIndex = cl.Index()
        vector = np.ones(1000000)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.atkinson(vector, 0.5) - 0.0) < ERROR_MARGIN)
        self.assertTrue(abs(myIndex.atkinson(vector, 1) - 0.0) < ERROR_MARGIN)
        self.assertTrue(abs(myIndex.atkinson(vector, 2) - 0.0) < ERROR_MARGIN)

    def test_atkinson(self):
        myIndex = cl.Index()
        vector = np.zeros(1000)
        vector[0] = 1
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.atkinson(vector, 2) - 1.0) < ERROR_MARGIN)

    def test_cr(self):
        """
        Testing Concentration Ratio

        """
        myIndex = cl.Index()
        n = 1000
        vector = np.ones(n)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.cr(vector, 1) - 1.0 / n) < ERROR_MARGIN)

    def test_bp(self):
        """
        Testing Berger-Parker

        """
        myIndex = cl.Index()
        n = 1000
        vector = np.ones(n)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.cr(vector, 1) - myIndex.berger_parker(vector)) < ERROR_MARGIN)

    def test_hhi(self):
        """
        Testing Herfindahl-Hirschman

        """
        myIndex = cl.Index()
        vector = np.ones(10)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.hhi(vector) - 0.0) < ERROR_MARGIN)

    def test_gini(self):
        """
        Testing Gini

        """
        myIndex = cl.Index()
        vector = np.ones(10)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.gini(vector) - 0.0) < ERROR_MARGIN)

    def test_shannon(self):
        """
        Testing Shannon

        """
        myIndex = cl.Index()
        vector = np.ones(10)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.shannon(vector) - 0.0) < ERROR_MARGIN)

    def test_hk(self):
        """
        Testing Hannah-Kay

        """
        myIndex = cl.Index()
        n = 10
        vector = np.ones(n)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.hk(vector, 1) - 1.0 / n) < ERROR_MARGIN)
        self.assertTrue(abs(myIndex.hk(vector, 3) - 1.0 / n) < ERROR_MARGIN)


class TestConfidenceIntervals(unittest.TestCase):
    """ Test confidence interval functionality

    """
    def shortDescription(self):
        doc = self._testMethodDoc
        return doc

    def test_ci_api(self):
        """
        Testing that all implemented indexes have monotonic confidence intervals

        """
        myIndex = cl.Index()
        portfolio = np.random.normal(loc=10, scale=1, size=100)

        methods = [['cr', 5], ['berger_parker'], ['hhi'], ['hk', 3],
                   ['hoover'], ['gini'], ['shannon'], ['atkinson', 1.5], ['gei', 3],
                   ['theil'], ['kolm', 2]]

        print(self.shortDescription())
        for method in methods:
            if len(method) > 1:
                lower_bound, value, upper_bound = myIndex.compute(portfolio, method[1], index=method[0], ci=0.95,
                                                                  samples=1000)
            else:
                lower_bound, value, upper_bound = myIndex.compute(portfolio, index=method[0], ci=0.95, samples=1000)
            self.assertTrue(lower_bound <= value)
            self.assertTrue(upper_bound >= value)


class TestEllisonGlaeser(unittest.TestCase):
    """ Test Ellison Glaeser index (multi-dimensional)

    """
    def shortDescription(self):
        doc = self._testMethodDoc
        return doc

    def test_eg_single_industry(self):
        """
        Testing EG Single Industry

        """
        myIndex = cl.Index()
        # Number of observations
        N = 10
        # Number of areas
        Na = 10
        # Number of industries
        Ni = 1
        # uniform exposure
        exposure = np.ones(N)
        # single industry
        industry = np.zeros(N, dtype=np.int)
        # uniform area distribution
        area = np.arange(0, N)
        # create dataframe
        d = {'Exposure': exposure, 'Area': area, 'Industry': industry}
        data = pd.DataFrame(data=d)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.ellison_glaeser(data, Na, Ni)[0] - 0.0) < ERROR_MARGIN)

    def test_eg_five_uniform(self):
        """
        Testing EG Five Uniform Industries

        """
        myIndex = cl.Index()
        # Number of observations
        N = 50
        # Number of areas
        Na = 10
        # Number of industries
        Ni = 5
        # uniform exposure
        exposure = np.ones(N)
        # single industry
        industry = np.array(list(np.arange(0, Ni)) * Na)
        # uniform area distribution
        y_list = [[j for i in range(Ni)] for j in range(Na)]
        area = np.array([y for x in y_list for y in x])
        # create dataframe
        d = {'Exposure': exposure, 'Area': area, 'Industry': industry}
        data = pd.DataFrame(data=d)
        results = myIndex.ellison_glaeser(data, Na, Ni)
        print(self.shortDescription())
        for i in range(Ni):
            self.assertTrue(abs(results[i] - 0.0) < ERROR_MARGIN)

    def test_eg_max_concentration(self):
        """
        Testing EG Maximum Concentration

        """
        myIndex = cl.Index()
        # Number of observations
        N = 400000
        # Number of areas
        Na = 200000
        # Number of industries
        Ni = 2
        # uniform exposure
        exposure = np.zeros(N)
        exposure[0:199999] = 1
        exposure[399999] = 1
        exposure[399998] = 0.0001

        # two industries
        area = np.array(list(np.arange(0, Na)) * Ni)
        # uniform area distribution
        y_list = [[j for i in range(Na)] for j in range(Ni)]
        industry = np.array([y for x in y_list for y in x])

        # create dataframe
        d = {'Exposure': exposure, 'Area': area, 'Industry': industry}
        data = pd.DataFrame(data=d)
        print(self.shortDescription())
        self.assertTrue(abs(myIndex.ellison_glaeser(data, Na, Ni)[0] - 0.0) < ERROR_MARGIN)


if __name__ == "__main__":
    unittest.main()
