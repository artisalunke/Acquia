.. include:: /common/global.rst

Message queue: Write adaptor
============================

The Message Queue Write Adaptor writes the selected record or field to
the message queue. The output will be written to the queue as JSON.

Creating the adaptor
--------------------

Create a **Queue** adaptor, and when it appears for configuration, in
the **Queue Action** list, be sure to click **Write**. For information
about creating or configuring adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

After you have created the adaptor, choose the data location of the data
that will be written to the queue. This must be a schema location or a
public variable.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Adaptor does not have           | It is necessary to create a       |
| connection set**                  | connection and choose it from the |
|                                   | **Adaptor Connection** drop down  |
+-----------------------------------+-----------------------------------+
| **This adaptor's configuration    | No data location for the message  |
| requires a data source to be      | to be written to the queue has    |
| set**                             | been chosen                       |
+-----------------------------------+-----------------------------------+
