## Concentration Library (CL)

A python library for the computation of various concentration indices.
The basic formulas of concentration metrics are simple and well known.

Dependencies: scipy, sympy

### Main Current Functions (concentration_library.py)

* Concentration Ratio
* Herfindahl-Hirschman Index
* Hannah-Kay Index
* Gini Index
* Shannon (Entropy) Index

### Testing 

Run test.py

### Usage

```
portfolio = np.random.zipf(a, 100)    
portfolio = sorted(portfolio, reverse=True)
weights = cl.weights(portfolio)
hhi = cl.hhi(weights)
gini = cl.gini(weights)
```

### Risk Forum 
Use the [forum](https://www.openrisk.eu/commons/forum/viewforum.php?f=20) for discussions

### Risk Manual
Use the [manual](https://www.openrisk.eu/commons/risk_manual/Main_Page) for documentation of use cases

### Contributions

If you want to contribute to CL please sign first the <a href="https://www.clahub.com/agreements/open-risk/OpenCPM">Contributor License Agreement</a>

Check the TODO list for ideas of where to take this library next
