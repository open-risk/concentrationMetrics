## Concentration Library (CL)

A python library for the computation of various concentration, diversification and inequality indices.

Dependencies: numpy, scipy

### Main Functions (concentration_library.py)

* Atkinson Index
* Concentration Ratio
* Berger-Parker Index
* Herfindahl-Hirschman Index
* Hannah-Kay Index
* Gini Index
* Theil Index
* Shannon Index
* Generalized Entropy Index
* Kolm Index

### Datasets

Version 0.2 includes two real datasets used for testing and comparison with R implementations

* hhbudget.csv
* Ilocos.csv

### Testing 

Run test.py

#### Comparison with R implementations

* atkinson_test.py compares the Atkinson function with the IC2/Atk function


### Usage

portfolio = np.random.zipf(a, 100)    
hhi = cl.hhi(portfolio)
gini = cl.gini(portfolio)

etc...

### Risk Forum 
Use the [forum](https://www.openrisk.eu/commons/forum/viewforum.php?f=20) for discussions

### Risk Manual
Use the [manual](https://www.openrisk.eu/commons/risk_manual/Main_Page) for documentation of use cases

### Contributions

Check the TODO list for ideas of where to take this library next
