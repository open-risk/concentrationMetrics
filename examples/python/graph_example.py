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

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import concentrationMetrics as cm

# Create a directed star graph
n = 101
# G = nx.star_graph(n, create_using=None)

G = nx.MultiDiGraph()
G.add_edges_from((0, i) for i in range(1, n))

# 0 is the central node
# for i in range(n):
#     print(nx.degree(G, i))

# Set edge attributes to random values representing contractual exposure
attrs = {}
for i in range(n):
    edge = (0, i, 0)
    attrs[edge] = {'exposure': np.random.randn()}
# print(attrs)

nx.set_edge_attributes(G, attrs)
#
# Set node attributes to random values representing credit risk
#
attrs = {}
for i in range(n):
    attrs[i] = {'rating': np.random.randn()}
print(attrs)
nx.set_node_attributes(G, attrs)

dataset_path = cm.source_path + "/datasets/"
nx.write_yaml(G, dataset_path + "star.yml")

# Load a graph
G1 = nx.read_yaml(dataset_path + "star.yml")
nx.draw(G1)
plt.show()

