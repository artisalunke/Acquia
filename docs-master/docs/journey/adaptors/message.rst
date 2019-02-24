.. include:: /common/global.rst

Message queue-related adaptors
==============================

.. toctree::
   :hidden:
   :glob:

   /journey/adaptors/message/*

You can combine your cloud service provider's message queuing service
with |acquia-product:aj|, enabling you to retrieve the next message from
your queue, publish a message through the queue, and poll for new
messages to drive your graph.

The following adaptors are available for you to interact with message
queues within your `graphs </journey/getting-started/graph>`__:

-  `Read </journey/adaptors/message/read>`__ - Retrieve the next
   available message from a queue
-  `Write </journey/adaptors/message/write>`__ - Publish a new message
   to a queue
-  `Listen </journey/adaptors/message/listen>`__ - Poll the message
   queue and process each message with your graph
