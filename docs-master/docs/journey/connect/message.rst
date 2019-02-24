.. include:: /common/global.rst

Message queue connection
========================

To use a message queue `adaptor </journey/adaptors>`__ with your
project, you must first configure a *message queue connection*, which is
a pair of queues acting as a read/write queue pair.

For information about creating, configuring, or testing connections, see
|connections|_.

.. |connections| replace:: Managing \ |acquia-product:aj| \ connections
.. _connections: /journey/connect

+-----------------+-----------------+-----------------+-----------------+
| Type of Queue   | Description     | Read Queue      | Write Queue     |
+=================+=================+=================+=================+
| Amazon SQS      | Amazon web      | Queue name —    | Queue name —    |
|                 | services simple | not the URL or  | not the URL or  |
|                 | queue service   | URN             | URN             |
+-----------------+-----------------+-----------------+-----------------+
| Active MQ       | Apache Active   | Queue name (for | Queue name (for |
|                 | MQ version 5.9  | example,        | example,        |
|                 | and greater     | ``dynamicQueues | ``dynamicQueues |
|                 |                 | /Q1``           | /Q1``           |
+-----------------+-----------------+-----------------+-----------------+
| Rabbit MQ       | Version 3 and   | Queue name      | Queue name      |
|                 | greater         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Azure Service   | Microsoft Azure | Queue name      | Queue name      |
| Bus             | cloud messaging |                 |                 |
|                 | service         |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

.. _fields:

Additional fields
-----------------

Depending on your **Type** selection, |acquia-product:aj| will display
the following additional fields:

-  *Amazon SQS*

   -  **AWS Access Key Id**
   -  **AWS Secret Access Key**
   -  **AWS Region** - One of the AWS regions (for example, us-east-1 or
      eu-west-1)

-  *Active MQ* or *Rabbit MQ*

   -  **User Name** - Username to connect to the queue, if required
   -  **Password** - Password to connect to the queue, if required
   -  **Host** - IP address or fully qualified domain name of the queue
      broker
   -  **SSL** - Click ``true`` if the queue is connected to using secure
      socket layers

-  *Azure Service Bus*

   -  **Key Name** - Name of the shared access policy associated with
      the queue
   -  **Key** - Primary or secondary key for the shared access policy
      associated with the queue
   -  **Namespace** - Service bus namespace
