Roadmap
============================

concentrationMetrics aims to become the reference python implementation for all widely used concentration and diversity indices and metrics. This roadmap lays out the upcoming steps in this journey.

An indicative list of future functionality to be implemented sometime within 2022

v0.6.xx
------------------------

* Network / Graph concentration indexes
* Further data sets to support network analysis

v0.7.xx
------------------------

* Spatial concentration indexes (distance based measures)
    * G-statistics, G*-statistics
    * Moran's I
    * Geary's C
    * Greenwood statistic
* Further visualization functionality

v0.8.xx
------------------------

* The aggregate data edge case (when part of the dataset has only aggregate, not individual data)
* Semantic self-documentation of metrics
* Focus on documentation



Todo List
==================
The concentrationMetrics library is an ongoing project. Several significant extensions are in the pipeline. Feature requests, bug reports and any other issues are welcome to log at the `Github Repository <https://github.com/open-risk/concentrationMetrics>`_

Discuss usage aspects of concentrationMetrics at the `Open Risk Commons <https://www.openriskcommons.org/t/concentration-measurement-using-python/76>`_

Further Concentration / Inequality / Diversity Indexes
------------------------------------------------------

- Streamline multiplicity of different naming conventions and normalizations
- Generalize the Shannon class to use different base calculations

Further Spatial / Multi-Group Concentrations Indexes
----------------------------------------------------

- Further indexes of the Ellison-Glaeser family

Implementation / Functionality
------------------------------

- Introduce visualization objects / API
- Better integration with pandas dataframes
- Streamline normalization / scaling of all indexes: Provide "standard" choice by default, offer additional options via parameter
- Add Lorenz curve functionality: Integrate Lorenz curve calculation / plotting along with Gini index
- Expand to cover categorical data use cases

Documentation
-------------
- Add Jupyter Notebook examples

Credit Risk Specific Functionality
----------------------------------
- Enable diversified portfolios