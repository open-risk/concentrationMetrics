# encoding: utf-8

# (c) 2017--2025 Open Risk (https://www.openriskmanagement.com), all rights reserved
#
# concentrationMetrics is licensed under the MIT license a copy of which is included
# in the source distribution of concentrationMetrics. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# Script to test concentrationMetrics against R packages

# ATTN: IC2 Package No Longer available on CRAN

# Script to test concentration library against R packages
# Package IC2
# Package ineq

library(IC2)
library(ineq)
data("hhbudgets")
calcAtkinson(hhbudgets[, "ingreso"], epsilon=0)
calcAtkinson(hhbudgets[, "ingreso"], epsilon=1)
calcAtkinson(hhbudgets[, "ingreso"], epsilon=2)
calcAtkinson(hhbudgets[, "ingreso"], epsilon=3)
calcAtkinson(hhbudgets[, "ingreso"], epsilon=4)


x <- c(541, 1463, 2445, 3438, 4437, 5401, 6392, 8304, 11904, 22261)
ineq(x)
ineq(x, parameter=0.5, type="Atkinson")
ineq(x, parameter=1.0, type="Atkinson")

write.table(hhbudgets,file="hhbudgets.csv",sep=",")

data(Ilocos)
attach(Ilocos)
income.p <- income[province=="Pangasinan"]/10000
income.u <- income[province=="La Union"]/10000
Lc.p <- Lc(income.p)
Lc.u <- Lc(income.u)

plot(Lc.p)
lines(Lc.u, col=2)

write.table(Ilocos,file="Ilocos.csv",sep=",")
