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
import pandas as pd

import concentrationMetrics as cm

myIndex = cm.Index()

# RANDOM PARETO EXPOSURES / UNIFORM INDUSTRIES)
# Number of observations
N = 100000
# Number of areas
Na = 5
# Number of industries
Ni = 3
# Pareto exposure distribution
a, m = 3., 2.  # shape and mode
exposure = (np.random.pareto(a, N) + 1) * m
# Uniform area distribution (276 NUTS 2 Regions)
area = np.random.randint(0, Na, N)
# Uniform industry distribution (21 NACE categories)
industry = np.random.randint(0, Ni, N)

# create dataframe
d = {'Exposure': exposure, 'Area': area, 'Industry': industry}
data = pd.DataFrame(data=d)
print(myIndex.ellison_glaeser(data, Na, Ni))
