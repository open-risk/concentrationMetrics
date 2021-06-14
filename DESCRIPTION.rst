The concentrationMetrics Library
================================

ConcentrationMetrics is an MIT-licensed `Python <http://www.python.org>`_ package aimed at becoming a reference implementation
of indexes used in the analysis of concentration, inequality and diversity measures.

Overview of Main Features
=========================

* exhaustive collection of concentration and inequality indexes and metrics
* supports file input/output in both json and csv formats
* detailed mathematical documentation
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

    # Calculate the desired indexes
    indices = Index()
    hhi = indices.hhi(portfolio)
    gini = indices.gini(portfolio)

    # Compute the confidence interval around the HHI index value
    lower_bound, val, upper_bound = indices.compute(portfolio, index='hhi', ci=0.95, samples=10000)

    # Calculate indexes on a dataframe
    BCI = pd.read_json(dataset_path + "BCI.json")
    y = BCI.values
    myGroupIndex = cm.Index(data=y, index='simpson')
    myGroupIndex.print(6)


Many more examples and tests are available in the examples and test directories.


File structure
==============

* `concentrationMetrics/model.py` The library module
* `datasets/` Contains a variety of datasets useful for getting started with the ConcentrationMetrics
* `examples/` Variety of usage examples
* `docs/` Sphinx generated documentation
* `tests/` testing the implementation

All indexes are currently implemented in concentrationMetrics/model.py as methods of the Index object.

Dependencies
============
The main dependencies are the standard python datascience stack (numpy, pandas etc) and networkx. The full list is in requirements.txt

- matplotlib
- numpy
- pandas
- scipy
- networkx

Datasets
========
Version 0.5.0 includes datasets used primarily for testing and comparison with R implementations:

- hhbudget.csv
- Ilocos.csv
- BCI.json

Testing
=======

Run python test.py

Comparison with R packages
=================================
-   atkinson\_test.py compares the Atkinson function with the IC2/Atk function
