Change Log
================================

PLEASE NOTE THAT THE API IS STILL UNSTABLE AS MORE USE CASES / FEATURES ARE ADDED REGULARLY

v0.6.0 (21-02-2022)
-------------------
* Installation:
    * PyPI release update


v0.5.1 (14-06-2020)
-------------------
* Added Hall-Tideman Index
* Streamlined input value exception handling (value / type errors), issue (https://github.com/open-risk/concentrationMetrics/issues/7)


v0.5.0 (05-04-2020)
-------------------
* Added script that produces cross-check calculations from corresponding R packages
* Expanded functionality to process dataframes
* First PyPI installation

v0.4.2 (08-03-2019)
-------------------

* Renamed library to concentrationMetrics to emphasize the nature of the library and follow the naming conventions of other Open Risk projects (transitionMatrix, correlationMatrix etc)
* Added readthedocs documentation

v0.4.1 (18-02-2019)
-------------------

* Provide confidence intervals via bootstraping
* Improved test documentation
* Fixed documentation links

v0.4 (17-08-2018)
-------------------
* Added new one-dimensional indexes: Hoover
* New multi-dimensional index family: Ellison-Glaeser
* Added normalized version flag (ranging in 0,1) for HHI, Shannon
* API Changes:
  * Introduction of Index object to organize different index calculations as methods
  * Lists are now converted to numpy arrays before processing
* More formal testing framework, added tests for the EG index

v0.3.1 (09-05-2018)
-------------------

* Code documentation via sphinx
* Improved alignment with Open Risk Manual pages

v0.3.0 (27-12-2017)
-------------------

* Exhaustive collection of indexes
* Direct documentation using Open Risk Manual URL's
* Simplification of the API (weight calculation by default)
* Visualizations
* Examples directory

v0.2.0 (23-11-2016)
-------------------

* First public release of the package