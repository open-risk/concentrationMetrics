======================
Concentration Library
======================

Concentration Library is an MIT-licensed `Python <http://www.python.org>`_
package aimed at becoming a reference implementation of indicators used in the analysis of concentration, inequality and diversity measures

Overview of Main Features
=========================

* exhaustive collection of concentration and inequality indexes and metrics
* supports file input/output in json and csv formats
* visualization using matplotlib


List of Implemented Indexes
===============================

An overview of the implemented metrics is available at the [Open Risk Manual](http://www.openriskmanual.org/wiki/Concentration_Index)

The below list provides specific documentation URL's for each one of the implement indexes

* [Atkinson Index](http://www.openriskmanual.org/wiki/Atkinson_Index)
* [Berger-Parker Index](http://www.openriskmanual.org/wiki/Berger-Parker_Index)
* [Concentration Ratio](http://www.openriskmanual.org/wiki/Concentration_Ratio)
* [Gini Index](http://www.openriskmanual.org/wiki/Gini_Index)
* [Theil Index](http://www.openriskmanual.org/wiki/Theil_Index)
* [Hannah-Kay Index](http://www.openriskmanual.org/wiki/Hannah_Kay_Index)
* [Herfindahl-Hirschman Index](http://www.openriskmanual.org/wiki/Herfindahl-Hirschman_Index)
* [Shannon Index](http://www.openriskmanual.org/wiki/Shannon_Index)
* [Generalized Entropy Index (Renyi)](http://www.openriskmanual.org/wiki/Generalized_Entropy_Index)
* [Kolm Index](http://www.openriskmanual.org/wiki/Kolm_Index)


Usage
===============================

Using the library is quite straightforward. For example calculating the Gini and the HHI indexes on randomly generated
portfolio data:

.. code:: python

    import concentration_library as cl
    import numpy
    a = 1.7
    portfolio = np.random.zipf(a, 100)
    hhi = cl.hhi(portfolio)
    gini = cl.gini(portfolio)


[A Comparison of HHI and Gini values for random portfolios](hhi_vs_gini.png)
