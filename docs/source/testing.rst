Testing
==================
Testing concentrationMetrics has two major components:

* normal code testing aiming to certify the correctness of code execution
* algorithm testing aiming to validate the correctness of algorithmic implementation

.. note:: In general algorithmic testing is not as precise as code testing and may be more subject to uncertainties such as numerical accuracy.


Running all the examples
------------------------
Running all the examples is a quick way to check that everything is installed properly, all paths are defined etc. At the root of the distribution:

.. code:: bash

    python3 run_examples.py


.. warning:: The script might generate a number of files / images at random places within the distribution


Test Suite
-------------
The testing framework is based on unittest.

Then run all tests

.. code:: bash

    python3 test.py

For an individual test:

.. code:: bash

    pytest tests/test_TESTNAME.py


