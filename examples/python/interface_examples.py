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

# Illustration of the various data formats that can be used
# Conversion to numpy array / matrices is required prior to calculation

# Reading data from a csv file via pandas
hhbudgets = pd.read_csv(cm.dataset_path + "hhbudgets.csv")

# Only the first column will be interpreted as data
y1a = hhbudgets["ingreso"]
print(myIndex.atkinson(data=y1a, epsilon=1))
y1b = hhbudgets[["ingreso", "transporte"]].values
print(myIndex.atkinson(y1b, 1))

# Using data in a numpy array
y2 = np.round(np.random.random((10, 3)) * 100).astype(int)
print(myIndex.atkinson(y2, 1))

# Using lists directly does now work
# y3 = [541, 1463, 2445, 3438, 4437, 5401, 6392, 8304, 11904, 22261]
# Convert to a numpy array first
y3 = np.array([541, 1463, 2445, 3438, 4437, 5401, 6392, 8304, 11904, 22261])
print(myIndex.atkinson(y3, 1))
