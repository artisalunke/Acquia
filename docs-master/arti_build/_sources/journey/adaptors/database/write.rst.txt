.. include:: /common/global.rst

Database: Write adaptor
=======================

The database Write Adaptor allows SQL ``INSERT`` or ``UPDATE`` queries
to be executed against a database.

Creating the adaptor
--------------------

`Create a Database adaptor </journey/adaptors#add>`__, and when it
appears for configuration, in the **Adaptor Action** list, be sure to
click **Write**. For more information about creating or configuring
adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

After you have created the adaptor, create the database query of one of
the two following forms:

-  ``INSERT INTO [(field1,field2, ...)] VALUES(field1, field2, ...)``
-  ``UPDATE  SET field1 = val1, field2 = val2, ... WHERE condition``

The SQL syntax should be kept generic. |acquia-product:aj| uses `SQL
Alchemy <http://www.sqlalchemy.org/>`__ to translate to the specific
database so there is no need to use database specific syntax. Any
parameters in the query are given in the form ``%%paramName%%``. The
closing semicolon is optional. Queries can be split over multiple lines
to increase readability.

For example to insert new records into a customer table the query could
be as follows:

``INSERT INTO customer(firstName,lastName,email) VALUES (%%firstName%%,%%lastName%%,%%email%%)``

It is not necessary to put quotation marks around the values in the
``VALUE`` statement or in a ``SET`` value if the values are simple
string values. However if the value is a JavaScript object or parent
schema location, then the quotation marks will be required.

Once the SQL has been edited, or a new parameter has been added, it is
necessary to click **Save Query / Update parameters**.

On Success the adaptor will return the number of changes records in the
optional **Records Changed** output location.

The database adaptor supports returning the value of an auto-increment
field in the **Records Changed** field and it will be returned in a
``primaryKey`` attribute as an array. If your table has a single
auto-increment field then it will be the zeroth element in the array.
Currently the only way to access that value is through a `JavaScript
Node </journey/node/javascript>`__ that returns the new value:

``newSchemaLocation = primaryKeys[0];``

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Adaptor does not have           | It is necessary to create a       |
| connection set**                  | connection and choose it from the |
|                                   | Adaptor Connection drop down      |
+-----------------------------------+-----------------------------------+
| **Database query cannot be        | The database query must have a    |
| empty**                           | valid SQL ``INSERT`` or           |
|                                   | ``UPDATE`` query                  |
+-----------------------------------+-----------------------------------+
| **Parameters each need a data     | Every parameter in the query of   |
| source**                          | the form ``%%param%%`` must be    |
|                                   | mapped to an input data source    |
+-----------------------------------+-----------------------------------+
