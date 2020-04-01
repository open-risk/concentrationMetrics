====================
ConcentrationMetrics
====================

ConcentrationMetrics is an MIT-licensed `Python <http://www.python.org>`_
package aimed at becoming a reference implementation of indicators used in the analysis of concentration,
inequality and diversity measures.

Overview of Main Features
=========================

* exhaustive collection of concentration and inequality indexes and metrics
* supports file input/output in both json and csv formats
* computation of confidence intervals via bootstraping
* visualization using matplotlib


Usage
===============================

Using the library is quite straightforward. For example calculating the Gini and the HHI indexes
on randomly generated portfolio data:

.. code:: python

    import numpy as np
    from concentrationMetrics import Index
    
    # Create some data
    a = 1.7
    portfolio = np.random.zipf(a, 100)

    # Calculate some indexes
    indices = Index()
    hhi = indices.hhi(portfolio)
    gini = indices.gini(portfolio)

    # Compute the confidence interval
    lower_bound, val, upper_bound = indices.compute(portfolio, index='hhi', ci=0.95, samples=10000)


Many more examples in the examples directory.


File structure
==============

* `concentrationMetrics.py` The library module
* `datasets/` Contains a variety of datasets useful for getting started with the ConcentrationMetrics
* `examples/` Variety of usage examples
* `docs/` Sphinx generated documentation
* `tests/` testing the implementation

All indexes are currently implemented in concentrationMetrics.py as methods of the Index object.

Dependencies
============

-   matplotlib
-   networkx
-   numpy
-   pandas
-   scipy

Datasets
========

Version 0.3.1 includes two real datasets currently used primarily for testing and comparison with R implementations:

-   hhbudget.csv
-   Ilocos.csv

Testing
=======

Run python test.py

Comparison with R implementations
=================================

-   atkinson\_test.py compares the Atkinson function with the IC2/Atk function
