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

import numpy as np

import concentrationMetrics as cm

dataset_path = cm.source_path + "datasets/"

# Bootstraped confidence intervals

# Select a portfolio of exposures

# Zipf distribution
# a = 1.7  # zipf parameter
# portfolio = np.random.zipf(a, 100)

# Normal distribution
portfolio = np.random.normal(loc=10, scale=1, size=100)

# Simple calculation
myIndex = cm.Index()
value = myIndex.compute(portfolio, index='hhi')
print('New API: ', value)
print("HHI Value ", myIndex.hhi(portfolio))

# Simple calculation with argument
value = myIndex.compute(portfolio, 3, index='hk')
print('New API: ', value)
print("HK Value ", myIndex.hk(portfolio, 3))

# Confidence interval calculation
lower_bound, value, upper_bound = myIndex.compute(portfolio, index='hhi', ci=0.95, samples=10000)
print("Lower Bound: ", lower_bound)
print("Value: ", value)
print("Upper Bound: ", upper_bound)
