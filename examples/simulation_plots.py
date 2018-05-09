# encoding: utf-8

# (c) 2017 Open Risk, all rights reserved
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
Purpose: Demonstrate usage of the Concentration Library
"""

import matplotlib.pyplot as plt
import numpy as np

import concentration_library as cl

if __name__ == "__main__":

# generate portfolio data (list)
# for some realism we use the Zipf power law

    a = 1.7 # zipf parameter
    x = []
    y = []
    for iter in range(0, 10000):  # portfolio simulations
        # Generate a portfolio of 100 entities
        portfolio = np.random.zipf(a, 100)    
        portfolio = sorted(portfolio, reverse=True)
        weights = cl.get_weights(portfolio)
        # Compute HHI and Gini indexes
        hhi = cl.hhi(weights)
        gini = cl.gini(weights)
        x.append(hhi)
        y.append(gini)
    # Plot values of HHI against Gini
    plt.style.use(['dark_background', 'ggplot'])
    plt.title('HHI versus Gini for random portfolios')
    plt.ylabel('Gini Index')
    plt.xlabel('Herfindahl-Hirschman Index')
    plt.scatter(y, x)
    plt.show()
