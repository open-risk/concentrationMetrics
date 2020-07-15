# encoding: utf-8

# (c) 2020 Open Risk, all rights reserved
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

# -*- coding: utf-8 -*-

"""Run all examples to test that everything is working with the current version."""

from concentrationMetrics import source_path

examples_path = source_path + "examples/python/"
filelist = ['atkinson_example', 'BCI_example', 'confidence_interval_example', 'ellison_glaeser_example', 'gini_example',
            'interface_examples', 'semantic_documentation', 'simulation_plots']

if __name__ == '__main__':

    for example in filelist:
        try:
            print('\nExecuting example file: ', example.upper())
            print('-----------------------' + '-' * len(example))
            exec(open(examples_path + example + ".py").read())
        except Exception:
            print('**********************' + '*' * len(example))
            print('ERROR in example file', example)
            print('**********************' + '*' * len(example))
