======================
Concentration Library
======================

Concentration Library is an MIT-licensed `Python <http://www.python.org>`_
package aimed at becoming a reference implementation of indicators used in the analysis of concentration, inequality and diversity measures

Overview of Main Features
=========================

* exhaustive collection of concentration and inequality indexes and metrics
* supports file input/output in both json and csv formats
* visualization using matplotlib


Usage
===============================

Using the library is quite straightforward. For example calculating the Gini and the HHI indexes on randomly generated
portfolio data:

.. code:: python

    import concentration_library as cl
    import numpy
    myIndex = cl.Index()
    a = 1.7
    portfolio = np.random.zipf(a, 100)
    hhi = myIndex.hhi(portfolio)
    gini = myIndex.gini(portfolio)


File structure
==============

* concentration\_library.py The library module
* datasets/ Contains a variety of datasets useful for getting started with the Concentration Library
* examples/ Variety of usage examples
* docs/ Sphinx generated documentation
* tests/ testing the implementation

All indexes are currently implemented in concentration\_library.py as methods of the Index object

Dependencies
============

-   numpy
-   pandas
-   scipy

Datasets
========

Version 0.3.1 includes two real datasets currently used primarily for testing and comparison with R implementations

-   hhbudget.csv
-   Ilocos.csv

Testing
=======

Run python test.py

Comparison with R implementations
=================================

-   atkinson\_test.py compares the Atkinson function with the IC2/Atk function