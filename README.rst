Concentration Library (CL)
==========================

A python library for the computation of various concentration, diversification and inequality indices.

| Created on Fri Nov 18 14:24:07 CET 2016
| Purpose: Concentration metrics library
| The library implements the computation of indexes of inequality and concentration. For
| each index, it provides decomposition between subgroups. Plotting of Lorenz and concentration
| curves are also available

[Full Description](DESCRIPTION.rst)

File structure
==============

| datasets/   Contains a variety of datasets useful for getting started with the Concentration Library
| examples/   Variety of usage examples
| docs/       Sphinx generated documentation
| concentration_library.py    The library

All functions are currently implemented in concentration_library.py

Dependencies
============

* numpy
* scipy


Datasets
===============================

Version 0.3.1 includes two real datasets currently used primarily for testing and comparison with R implementations

* hhbudget.csv
* Ilocos.csv

Testing
===============================

Run test.py

Comparison with R implementations
=================================

* atkinson_test.py compares the Atkinson function with the IC2/Atk function

Contributions
===============================

Check the [TODO list](TODO.rst) for ideas of where to take this library next
