Data Preparation
================

Vector Data
-----------
The basic index calculation assumes that data are provided in a vector format (more precisely a numpy 1d-array). If you starting point has the data in a different format you will need to preprocess the data to bring it to this form.

The data type can be integer (e.g. count of individuals of some type) or float (e.g. exposure, amount, size etc.)

The data need not be normalized, this is done automatically with the :meth:`concentrationMetrics.model.Index.get_weights` method. (This is an idempotent operation: Applying the method on already normalized data is not a problem)

Tabular Data and Dataframes
---------------------------
For convenience, when the data are in tabular or dataframe format (e.g. observation counts for different types of entities) the library offers built-in functionality to calculate metrics across the data set. So for example if we have the distribution of counts per Attribute (rows) for three distinct categories (Columns Group 1 to 3) the calculation will produce the desired index for each one of the Groups


+-----------+------------+------------+
| Group 1   | Group 2    | Group 3    |
+-----------+------------+------------+
| Count     | Count      |  Count     |
+-----------+------------+------------+
| Count     | Count      |  Count     |
+-----------+------------+------------+
| ...       | ...        |  ...       |
+-----------+------------+------------+
| Count     | Count      |  Count     |
+-----------+------------+------------+

