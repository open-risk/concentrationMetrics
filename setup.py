# encoding: utf-8

# (c) 2017-2022 Open Risk (https://www.openriskmanagement.com)
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


from codecs import open
from setuptools import setup

__version__ = '0.6.0'

ver = __version__

long_descr = open('docs/source/description.rst', 'r', encoding='utf8').read()

setup(
    name='concentrationMetrics',
    version=ver,
    description='A python library for the computation of various concentration, inequality and diversity indices',
    long_description=long_descr,
    long_description_content_type='text/x-rst',
    author='Open Risk',
    author_email='info@openrisk.eu',
    packages=['concentrationMetrics', 'datasets', 'examples.python'],
    include_package_data=True,
    url='https://github.com/open-risk/concentrationMetrics',
    download_url='https://github.com/open-risk/concentrationMetrics/archive/v_0.5.0.tar.gz',
    license='The MIT License (MIT)',
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'networkx',
        'pytest'
    ],
    zip_safe=False,
    provides=['concentrationMetrics'],
    keywords=['concentration', 'diversity', 'inequality', 'index'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]
)
