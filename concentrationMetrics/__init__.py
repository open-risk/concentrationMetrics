# encoding: utf-8

# (c) 2017-2022 Open Risk (www.openriskmanagement.com), all rights reserved
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


""" concentrationMetrics - Python package aimed at becoming a reference implementation of indicators used in the
analysis of concentration, inequality and diversity measures. """

from .model import *

__version__ = '0.5.0'

package_name = 'concentrationMetrics'
module_path = os.path.dirname(__file__)
source_path = module_path[:-len(package_name)]
dataset_path = os.path.join(source_path, 'datasets/')
