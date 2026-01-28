# encoding: utf-8

# (c) 2017--2026 Open Risk (https://www.openriskmanagement.com), all rights reserved
#
# concentrationMetrics is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of concentrationMetrics. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

"""
Run the concentrationMetrics unittest suite

"""

import sys
import unittest

from concentrationMetrics import source_path

sys.path.append(source_path)

loader = unittest.TestLoader()
start_dir = source_path + '/tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)
