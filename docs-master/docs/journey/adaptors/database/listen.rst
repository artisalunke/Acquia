.. include:: /common/global.rst

Database: Listen adaptor
========================

The database listen adaptor allows a database table to act as a queue of
items to be processed. The listen adaptor repeatedly queries the
database with a ``SELECT`` statement at specified intervals, then
returns up to a maximum number of records to be processed by the graph.
Following a successful query, a ``SET`` statement is issued to stop the
process repeatedly retrieving the same records.

Creating the adaptor
--------------------

To create a database listen adaptor it is best practice, but not
necessary, to create a `database
connection </journey/connect/database>`__. To create the database listen
adaptor on any graph, complete the following actions:

#. Sign in to |acquia-product:aj|.
#. Click the |acquia-product:aj| logo in the top menu to view the main
   project page.
#. Identify the project that you want to modify, and then click its
   **Project Editor** |Project Editor icon| icon.
#. Select the graph to which you want to add a listener, and then click
   **Open** at the bottom of the panel.
#. In the top right of the graph editing canvas, click **Add Listener**.
   |acquia-product:aj| will display the **Listener** dialog box. |Listen
   adaptor dialog|
#. In the **Adaptor Connection (Environment)** list, either click the
   connection that you want to use, or edit it directly by clicking the
   **Pencil** icon next to the connection name.
#. In the **Listen Query** area, specify a ``SELECT`` statement without
   joins or nested queries that will evaluate a timestamp or flag on the
   table to determine which records to return for processing. The
   ``SELECT`` statement must be of the form
   ``SELECT ... FROM ... WHERE ...`` with the ``WHERE`` clause selecting
   only unprocessed records. See the following section for `additional
   information about creating queries <#writing>`__.
#. In the **Set Statement** field, enter a ``SET`` statement that
   updates the selected records to prevent reprocessing. See the
   following section for `additional information about creating
   queries <#writing>`__.
   |acquia-product:aj| returns the records that match each query to the
   **Records Selected** output destination.
#. Optionally, set the values for the following items:

   -  **Listen Interval (seconds)** - The whole number of seconds
      between SELECT statements to the database. *(Default: 1 second)*
   -  **Max Record Count** - The maximum number of records the listener
      will return in one query, ensuring multiple threads may run
      simultaneously without a single request attempting to return all
      records.

#. Click **Save**.

The listen operation is thread-safe and is able to execute in multiple
instances without each operation returning the same records.

Writing queries
---------------

Regardless of the query that you create for listen queries and set
statements, you can omit the semi-colon ( ``;`` ) from the end of each
statement.

A *listen query* may specify fields as part of the ``SELECT`` clause
(``SELECT field1, field2 FROM ...``) or include all fields in a record
by specifying the asterisk ( ``*`` — for example,
``SELECT * FROM ...``). Each field is mapped to your `data schema or
public variable </journey/data>`__. If a field in a retrieved record
does not exist in your data schema or public variable,
|acquia-product:aj| will create the field for you.

A *set statement* can set only a constant value. |acquia-product:aj|
sets the ``WHERE`` portion of the statement for you based on the records
retrieved from the listen query. You cannot use any database stored
procedures in your query.

Example queries
---------------

The following example evaluates for a ``processed`` flag to identify
new, unprocessed, records:

``SELECT id,firstname,lastname,email FROM customer WHERE processed = 'N';``

To set the ``processed`` flag on records, use a query similar to the
following:

``SET processed = 'Y';``

Validation warnings
-------------------

Attempting to save a database listen adaptor without completing all of
its necessary values will return one or more of the following
notifications:

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Database Listener must have an  | It is necessary to select an      |
| Output**                          | output location for the Listen    |
|                                   | Adaptor                           |
+-----------------------------------+-----------------------------------+
| **Database Listener must have an  | A listen and and update query     |
| Update Query**                    | must be provided                  |
+-----------------------------------+-----------------------------------+
| **Database Listener must have a   | No connection has been selected   |
| Connection set**                  |                                   |
+-----------------------------------+-----------------------------------+

.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Listen adaptor dialog| image:: https://cdn3.webdamdb.com/1280_QJHc7KB3nBO9.png?1526475712
   :width: 500px
