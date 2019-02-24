.. include:: /common/global.rst

Database: Delete adaptor
========================

The database delete adaptor allows SQL ``DELETE`` statements to be
executed. The number of records deleted by the ``DELETE`` statement will
be put into the output destination schema or public variable location.

Creating the adaptor
--------------------

`Create a Database adaptor </journey/adaptors#add>`__, and when it
appears for configuration, in the **Adaptor Action** list, be sure to
click **Delete**. For more information about creating or configuring
adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

After you have created the adaptor, the ``DELETE`` query should be
specified as a standard SQL expression. |acquia-product:aj| uses the
Python SQL Alchemy library to convert the SQL to the specific dialect of
the database type, so there is no need to used database specific
encoding such as backticks (:literal:`\`example\``) for MySQL or square
brackets (``[example]``) for Microsoft SQL. It is good practice to
develop your query and ensure that it returns the correct data in your
usual database development tool before copying to |acquia-product:aj|
and parameterizing.

Final semi-colons are optional. The query can be split over several
lines for readability purposes.

The query can be parameterized using ``%%paramName%%`` anywhere within
the query. For example, a query to select a customer record could look
as follows:

``DELETE from appParams WHERE paramKey = '%%paramKey%%';``

Strings included in ``WHERE`` clauses should use single ( ``'`` ) or
double ( ``"`` ) quotation marks. If the parameter is numeric, quotation
marks are not required.

Whenever the query is changed and a parameter is added or removed, you
must save your query by clicking **Save Query / Update Parameters**.
Saving your query will both identify all of the parameters and will
create a slot for this query in the Parameters list in the bottom left
panel.

After you have specified parameter locations in your query, you can test
your query. |acquia-product:aj| will validate your query before
executing the test. If the adaptor displayed in the example executes
successfully, it will populate the schema with the number of deleted
rows:

``{ "dbResponse": 1 }``

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Parameters each need a data     | Every parameter in the query of   |
| source**                          | the form ``%%param%%`` must be    |
|                                   | mapped to an input data source    |
+-----------------------------------+-----------------------------------+
