# encoding: utf-8

# (c) 2015-2017 Open Risk, all rights reserved
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

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import concentration_library as cl

dataset_path = cl.source_path + "datasets/"

Ilocos = pd.read_csv(dataset_path + "Ilocos.csv")

values = {'ids': ['province'], 'vals': ['Pangasinan']}

# print(Ilocos)
# income = Ilocos.as_matrix(columns=["income"])
income_p = Ilocos[Ilocos['province'] == 'La Union']
# p = income_p.as_matrix(columns=["income"])
p = income_p["income"].values
p = np.divide(p, 10000)
n = p.size
F = np.divide(np.arange(n+1), n)
p.sort()
S = np.empty(n+1)
S[0] = 0
S[1:] = np.divide(p.cumsum(), np.sum(p))


plt.figure()
lw = 2
plt.plot(F, S, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % 0.5)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='-')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('Cumulative Population Fraction')
plt.ylabel('Cumulative Attribute Fraction')
plt.title('Lorenz Curve')
plt.legend(loc="lower right")
plt.show()