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

import concentrationMetrics as cm
import numpy as np

myIndex = cm.Index()
x = np.array([541, 1463, 2445, 3438, 4437, 5401, 6392, 8304, 11904, 22261])


# Comparison with R version in ineq package
# Results
# Gini:             0.4620911
# Atkinson a=0.5:   0.1796591
# Atkinson a=1:     0.3518251

print(myIndex.gini(x))
print(myIndex.atkinson(x, 0.5))
print(myIndex.atkinson(x, 1.0))
