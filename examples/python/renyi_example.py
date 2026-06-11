# encoding: utf-8

# (c) 2016--2026 Open Risk (https://www.openriskmanagement.com), all rights reserved
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

"""
Rényi Entropy example.

Reference: Rényi, A. (1961), "On measures of entropy and information",
Proceedings of the 4th Berkeley Symposium on Mathematics, Statistics and Probability,
Vol. 1, pp. 547-561.

Key properties illustrated:
- For a uniform distribution of n elements, H_alpha = log(n) for all alpha >= 0.
- At alpha=1, the Rényi entropy equals the Shannon entropy.
- At alpha=2, H_2 = -log(HHI_unnormalized).
- Higher alpha places more weight on the dominant share (lower entropy = more concentrated).
"""

import numpy as np

import concentrationMetrics as cm

myIndex = cm.Index()

# --- Uniform distribution (4 equally-sized entities) ---
print("Uniform distribution, n=4")
vector_uniform = np.ones(4)
for alpha in [0, 0.5, 1, 2, 3]:
    print(f"  H_{alpha} = {myIndex.renyi(vector_uniform, alpha):.6f}  (log(4) = {np.log(4):.6f})")

print()

# --- Concentrated distribution (one dominant entity) ---
print("Concentrated distribution: [10, 1, 1, 1, 1]")
vector_skewed = np.array([10.0, 1.0, 1.0, 1.0, 1.0])
for alpha in [0, 1, 2, 5]:
    print(f"  H_{alpha} = {myIndex.renyi(vector_skewed, alpha):.6f}")

print()

# --- Relationship to HHI at alpha=2 ---
print("Relationship H_2 = -log(HHI_unnormalized) for uniform n=4:")
hhi_raw = myIndex.hhi(vector_uniform, normalized=False)
print(f"  HHI (unnormalized) = {hhi_raw:.6f}")
print(f"  -log(HHI)          = {-np.log(hhi_raw):.6f}")
print(f"  H_2 (Rényi)        = {myIndex.renyi(vector_uniform, 2):.6f}")

print()

# --- Confidence interval for Rényi entropy at alpha=2 ---
print("Bootstrap 95% CI for H_2 on a simulated portfolio (n=100):")
portfolio = np.random.lognormal(mean=0, sigma=1, size=100)
lower, value, upper = myIndex.compute(portfolio, 2, index='renyi', ci=0.95, samples=1000)
print(f"  [{lower:.4f}, {value:.4f}, {upper:.4f}]")
