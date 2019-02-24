.. include:: /common/global.rst

Database: Read adaptor
======================

The *database read adaptor* allows SQL Select statements to be executed.
The records returned by the Select statement will be put into the output
destination schema or public variable location.

Creating the adaptor
--------------------

`Create a Database adaptor </journey/adaptors#add>`__, and when it
appears for configuration, in the **Adaptor Action** list, be sure to
click **Read**. For more information about creating or configuring
adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

After you have created the adaptor, the **Read Query** should be
specified as a standard SQL expression. |acquia-product:aj| uses the
Python SQL Alchemy library to convert the SQL to the specific dialect of
the database type. So there is no need to used database specific
encoding such as backticks (:literal:`\`identifier\``) for MySQL or
square brackets (``[identifier]``) for Microsoft SQL. It is good
practice to develop your query and ensure that it returns the correct
data in your usual database development tool before copying to
|acquia-product:aj| and parameterizing.

Final semi-colons are optional. The query can be split over several
lines for readability purposes.

The query can be parameterized using ``%%paramName%%`` anywhere within
the query. For example, an entry in the **Read Query** area to select a
customer record could look as follows:

``select firstName, lastName, email from customer where IdCustomer = %%customerId%%``

Anything used in a ``WHERE`` clause for a ``SELECT`` statement should
use single or double quotes if the parameter is a string. If the
parameter is numeric as shown in the above query quotation marks are not
required.

``select * from appParams where paramKey like '%%paramKey%%';``

Whenever the query is changed and a parameter is added or removed, it is
necessary to save the query by clicking **Save Query / Update
Parameters**. This will identify all of the parameters and create a slot
for this in the **Parameters** list in the bottom left panel.

After all of the parameter locations have been specified, the adaptor
will become valid.

If this adaptor executes successfully, it will populate the schema as
follows:

-  Data Store Values

   -  Schema

      -  customer

         -  lastName : Smith
         -  email : jsmith@example.com
         -  firstName : Jay

   -  Public Variables

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Parameters each need a data     | Every parameter in the query of   |
| source**                          | the form ``%%param%%`` must be    |
|                                   | mapped to an input data source    |
+-----------------------------------+-----------------------------------+
