.. include:: /common/global.rst

Message queue: Read adaptor
===========================

The Message Queue Read Adaptor reads the next available message from the
message queue. If the message is in JSON format then it will be parsed
and mapped to the correct fields in the output record.

Creating the adaptor
--------------------

Create a **Queue** adaptor, and when it appears for configuration, in
the **Queue Action** list, be sure to click **Read**. For information
about creating or configuring adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

The Message Queue Read Adaptor will return an error if there is no
message on the queue.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Adaptor does not have           | It is necessary to create a       |
| connection set**                  | connection and choose it from the |
|                                   | **Adaptor Connection** list.      |
+-----------------------------------+-----------------------------------+
| **Missing data                    | No data destination for the       |
| destination/output**              | message read from the queue has   |
|                                   | been specified.                   |
+-----------------------------------+-----------------------------------+
