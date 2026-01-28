# encoding: utf-8

# (c) 2017--2026 Open Risk (https://www.openriskmanagement.com), all rights reserved
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
# Package IC2
# Package ineq
# Package vegan
# Package EcoIndR

# IC2 Package No Longer available on CRAN

library(IC2)
data(hhbudgets)

decompAtkinson(hhbudgets[,"ingreso"], hhbudgets[,"estructura"], epsilon=3)
summary(hhbudgets[,"tenencia"]) # 35 NA's
summary(decompAtkinson(x=hhbudgets[,"transporte"], z=hhbudgets[,"tenencia"], w=hhbudgets[,"factor"], decomp="DP", ELMO=FALSE))
summary(decompAtkinson(x=hhbudgets[,"transporte"], z=hhbudgets[,"tenencia"], w=hhbudgets[,"factor"], decomp="DP", epsilon=0.25))

decompGEI(hhbudgets[,"ingreso"], hhbudgets[,"estructura"], alpha=4)
summary(hhbudgets[,"tenencia"]) #35 NA's
decompGEI(x=hhbudgets[,"transporte"], z=hhbudgets[,"tenencia"], w=hhbudgets[,"factor"], ELMO=FALSE)
summary(decompGEI(x=hhbudgets[,"transporte"], z=hhbudgets[,"tenencia"], w=hhbudgets[,"factor"], alpha=1.5))

library(vegan)
data(BCI)
H <- diversity(BCI)
simp <- diversity(BCI, "simpson")
invsimp <- diversity(BCI, "inv")
shannon <- diversity(BCI, "shannon")

knitr::kable(head(shannon))