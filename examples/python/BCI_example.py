# encoding: utf-8

# (c) 2020 Open Risk, all rights reserved
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
import pandas as pd

dataset_path = cm.source_path + "/datasets/"

# Comparison with R version in vegan package on BCI dataset

"""
|   Simpson|
|---------:|
| 0.9746293|
| 0.9683393|
| 0.9646078|
| 0.9716117|
| 0.9678267|
| 0.9627557|

|Inv Simpson|
|--------:|
| 39.41555|
| 31.58488|
| 28.25478|
| 35.22577|
| 31.08166|
| 26.84973|

|  Shannon|
|--------:|
| 4.018412|
| 3.848471|
| 3.814059|
| 3.976563|
| 3.969940|
| 3.776575|

"""


BCI = pd.read_json(dataset_path + "BCI.json")
y = BCI.values

# Dataframe API
myGroupIndex = cm.Index(data=y, index='simpson')
myGroupIndex.print(6)

myGroupIndex = cm.Index(data=y, index='invsimpson')
myGroupIndex.print(6)

myGroupIndex = cm.Index(data=y, index='shannon')
myGroupIndex.print(6)

# Columnwise API
mySingleIndex = cm.Index()
for i in range(6):
    print('HHI')
    print('----------')
    print(i, mySingleIndex.hhi(y[i, :]))

