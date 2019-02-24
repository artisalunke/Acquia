.. include:: /common/global.rst

Message queue: Listen adaptor
=============================

The message queue listen adaptor allows a graph to listen to messages
arriving in a message queue and process them. The listen adaptor
continuously polls the queue for new messages. The poll interval can be
specified in the adaptor.

Creating the adaptor
--------------------

To create the message queue listen adaptor on any graph, complete the
following steps:

.. note::
  To create a message queue listen adaptor it is best practice, but not
  necessary, to create a `database
  connection </journey/connect/database>`__.

#. Click **Add** in the top right of a graph window.
   This will display the Listener configuration dialog.
#. In the **Adaptor Connection (Environment)** list, either click the
   connection that you want to use or edit it directly by clicking the
   pencil icon next to the connection name
#. Specify the **Listen Interval** in seconds.
#. Choose the target location for the output from the queue.
#. Click **Save**.

Validation warnings
-------------------

Attempting to save the message queue listen adaptor without completing
all of the necessary parts will create one or more notifications:

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Queue Listener must have a      | No connection has been selected.  |
| Connection set**                  |                                   |
+-----------------------------------+-----------------------------------+
| **Queue Listener must have an     | The queue listener needs a        |
| Output**                          | location to write the incoming    |
|                                   | records to.                       |
+-----------------------------------+-----------------------------------+
