# encoding: utf-8

# (c) 2016-2022 Open Risk, all rights reserved
#
# ConcentrationMetrics is licensed under the MIT license a copy of which is included
# in the source distribution of concentrationMetrics. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
"""
@author: Open Risk
Purpose: Demonstrate usage of the ConcentrationMetrics
"""

import matplotlib.pyplot as plt
import numpy as np

import concentrationMetrics as cm

if __name__ == "__main__":

    # generate portfolio data (list)
    # for some realism we use the Zipf power law

    myIndex = cm.Index()

    a = 1.7  # zipf parameter
    x = []
    y = []
    for iteration in range(0, 10000):  # portfolio simulations
        # Generate a portfolio of 100 entities
        portfolio = np.random.zipf(a, 100)
        portfolio = np.array(sorted(portfolio, reverse=True))
        # Compute HHI and Gini indexes
        hhi = myIndex.hhi(portfolio)
        gini = myIndex.gini(portfolio)
        x.append(hhi)
        y.append(gini)
    # Plot values of HHI against Gini
    plt.style.use(['dark_background', 'ggplot'])
    plt.title('HHI versus Gini for random portfolios')
    plt.ylabel('Gini Index')
    plt.xlabel('Herfindahl-Hirschman Index')
    plt.scatter(y, x)
    plt.show()
