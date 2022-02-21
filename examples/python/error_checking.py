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

y = [0, 1, 2, 3]  # this throws a numpy AttributeError
# y = [-1, 1, 2, 3]  # this throws a ValueError (data values must be positive)
# y = [0, 0, 0, 0]  # this throws a ValueError (some data values must be non-zero)
# y = [0, 1, 2, 3, 4]
y = np.array(y)

myIndex = cm.Index()
print(myIndex.atkinson(y, 1))

