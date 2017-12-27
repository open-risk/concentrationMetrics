## Concentration Library (CL)

A python library for the computation of various concentration, diversification and inequality indices.

[Full Description](DESCRIPTION.rst)

### List of Implemented Indexes

All functions are currently implemented in concentration_library.py
The below list provides documentation URL's for each one of the implement indexes

* [Atkinson Index](http://www.openriskmanual.org/wiki/Atkinson_Index)
* [Concentration Ratio](http://www.openriskmanual.org/wiki/Concentration_Ratio)
* [Berger-Parker Index](http://www.openriskmanual.org/wiki/Concentration_Ratio)
* [Herfindahl-Hirschman Index](http://www.openriskmanual.org/wiki/Herfindahl-Hirschman_Index)
* [Hannah-Kay Index](http://www.openriskmanual.org/wiki/Hannah_Kay_Index)
* [Gini Index](http://www.openriskmanual.org/wiki/Gini_Index)
* [Theil Index](http://www.openriskmanual.org/wiki/Theil_Index)
* [Shannon Index](http://www.openriskmanual.org/wiki/Shannon_Index)
* [Generalized Entropy Index](http://www.openriskmanual.org/wiki/Generalized_Entropy_Index)
* [Kolm Index](http://www.openriskmanual.org/wiki/Kolm_Index)

### Datasets

Version 0.3 includes two real datasets used for testing and comparison with R implementations

* hhbudget.csv
* Ilocos.csv

### Testing 

Run test.py

#### Comparison with R implementations

* atkinson_test.py compares the Atkinson function with the IC2/Atk function


### Usage

Using the library is quite straightforward. For example calculating the Gini and the HHI
indexes

```python
import concentration_library as cl
import numpy
a = 1.7
portfolio = np.random.zipf(a, 100)    
hhi = cl.hhi(portfolio)
gini = cl.gini(portfolio)
```

[A Comparison of HHI and Gini values for random portfolios](hhi_vs_gini.png)


### Contributions

Check the [TODO list](TODO.rst) for ideas of where to take this library next
